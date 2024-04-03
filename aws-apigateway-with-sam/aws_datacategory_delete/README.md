# Data Processing Lambda

This Lambda function is responsible for processing data types.

## Functionality

- Receives an event containing data parameters.
- Validates the parameters.
- Logs the processing steps.
- Saves the data on S3.
- Modifies the data in a database table.
- Handles errors and exceptions gracefully.

## Setup

1. Ensure AWS credentials are properly configured.
2. Create necessary IAM roles and policies.
3. Deploy the Lambda function using AWS CLI or AWS Management Console.
4. Set up necessary environment variables such as `SECRET_LAMBDA`, `CON_REDSHIFT_DEV`, `LOGZ_TOKEN`, and `S3_BUCKET`.
5. Ensure the required Python packages are installed.
6. Configure Logz.io and AWS Secrets Manager if applicable.
