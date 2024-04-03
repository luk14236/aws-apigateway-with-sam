import datetime
import logging
import json
import os
import boto3
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from logzio.flusher import LogzioFlusher
from botocore.exceptions import ClientError

# Configuring logger
def configure_logger(logz_token):
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'logzioFormat': {
                'format': '{"additional_field": "value"}',
                'validate': False
            }
        },
        'handlers': {
            'logzio': {
                'class': 'logzio.handler.LogzioHandler',
                'level': 'INFO',
                'formatter': 'logzioFormat',
                'token': logz_token,
                'logzio_type': 'python-handler',
                'logs_drain_timeout': 5,
                'url': 'https://listener-eu.logz.io:8071'
            }
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['logzio'],
                'propagate': True
            }
        }
    }

    logging.config.dictConfig(logging_config)
    return logging.getLogger('superAwesomeLogzioLogger')

# Getting secret from AWS Secrets Manager
def get_secret(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)

    try:
        response = client.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
    except ClientError as e:
        raise e

    return json.loads(secret)

# Creating path for the lake
def create_lake_path(data_point, file_name):
    now = datetime.datetime.now()
    path = f"{data_point}/{now.year}/{now.month}/{now.day}/{now.hour}/{now.minute}/{file_name}"
    return path

# Main Lambda function
@LogzioFlusher(logger)
def lambda_handler(event, context):
    event_query = event['queryStringParameters']
    event_parameter = event_query['data_id']

    if not event_parameter:
        return {"statusCode": 422, "body": "Wrong payload"}

    # Initializing database session
    secret = get_secret("SECRET_LAMBDA", "eu-central-1")
    engine = create_engine(json.loads(secret)["CON_REDSHIFT_DEV"])
    db = scoped_session(sessionmaker(bind=engine))

    try:
        # Saving to the lake
        s3 = boto3.resource('s3')
        lake_key = create_lake_path('data-category', f"data-category-data-type-delete-{datetime.datetime.now()}.json")
        s3.Object(os.environ["S3_BUCKET"], lake_key).put(Body=bytes(event_parameter.encode('UTF-8')))

        # Deleting from the database
        delete_data_type_query = f"""
            DELETE FROM data_category
            WHERE data_id = {event_parameter};
        """
        db.execute(delete_data_type_query)
        db.commit()

        # Log entry
        logger.info("Data type deleted", extra={"service": "Data Processing", "data_category": "DATA TYPE", "action": "DELETE", "statusCode": 204})

        result = {"body": json.dumps({"service": "Data Processing", "data_category": "DATA TYPE", "action": "DELETE", "message": "Data type deleted"}), "statusCode": 204}
        
    except Exception as ex:
        logger.error(str(ex), extra={"service": "Data Processing", "data_category": "DATA TYPE", "action": "DELETE", "payload": event_parameter, "statusCode": 500})
        result = {"body": json.dumps({"service": "Data Processing", "data_category": "DATA TYPE", "action": "DELETE", "payload": event_parameter, "message": str(ex)}), "statusCode": 500}
        
    finally:
        db.close()

    return result
