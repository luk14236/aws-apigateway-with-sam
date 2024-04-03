# Lambda Function: Data Processing

This Lambda function processes incoming data and stores it in an AWS S3 bucket and a relational database.

## Functionality

- Retrieves secret values from AWS Secrets Manager for database connection.
- Configures a logger for logging using Logz.io.
- Processes incoming data payload and checks for required fields.
- Stores the data payload in an S3 bucket.
- Inserts the data into a relational database.
- Logs information about the processing.

## Usage

1. Ensure that AWS Secrets Manager is properly configured with the required secret values.
2. Set up an S3 bucket for storing the processed data.
3. Configure a relational database with the appropriate table structure.
4. Deploy this Lambda function in your AWS account.
5. Configure the necessary environment variables such as S3 bucket name and Logz.io token.
6. Trigger the Lambda function with appropriate data payloads.

## Dependencies

- Python 3.7 or higher
- SQLAlchemy
- Logz.io Python SDK
- Boto3

## Environment Variables

- `SECRET_LAMBDA`: The name of the secret in AWS Secrets Manager containing database connection details.
- `S3_BUCKET`: The name of the S3 bucket where the data will be stored.

## Logging

This Lambda function logs information using Logz.io for monitoring and debugging purposes.

