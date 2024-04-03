# Data Processing Lambda

This Lambda function processes data types.

## Functionality

- Receives an event with data parameters.
- Validates parameters.
- Logs processing steps.
- Saves data to S3.
- Modifies data in a database table.
- Handles errors and exceptions.

## Setup

1. Configure AWS credentials.
2. Create necessary IAM roles and policies.
3. Deploy Lambda function using AWS CLI or Management Console.
4. Set environment variables:
   - `SECRET_LAMBDA`: AWS Secrets Manager secret containing sensitive information.
   - `CON_REDSHIFT_DEV`: Database connection details.
   - `LOGZ_TOKEN`: Token for Logz.io logging.
   - `S3_BUCKET`: Name of the S3 bucket for data storage.
5. Install required Python packages.
6. Configure Logz.io and AWS Secrets Manager if needed.
