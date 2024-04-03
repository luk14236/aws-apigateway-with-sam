# AWS Data Processing

This repository contains code and configuration for AWS Lambda functions responsible for processing data related to data categories. It includes the following features:

- **Create Data Category:** Lambda function to create a new data category in Redshift and stream the data to an S3 data lake.
- **Update Data Category:** Lambda function to update an existing data category in Redshift and log the update action.
- **Delete Data Category:** Lambda function to delete a data category from Redshift and log the deletion action.
- **Logging:** Integration with Logz.io for logging Lambda function activities.
- **Error Handling:** Comprehensive error handling and logging for better troubleshooting.

## Usage

1. Clone this repository to your local machine.
2. Customize the Lambda functions as needed for your environment and requirements.
3. Deploy the Lambda functions using AWS SAM CLI by running `sam build` followed by `sam deploy --guided`.
4. Once deployed, you will get the endpoints for your API Gateway. These endpoints can be used to trigger the Lambda functions.

## Prerequisites

Before using this project, make sure you have the following prerequisites installed/configured:

- AWS CLI configured with appropriate permissions.
- Python 3.8 or higher installed locally.
- AWS SAM CLI installed.
- AWS Secrets Manager configured with necessary secrets.
- Logz.io account with token for logging Lambda activities.

## Testing

This project includes feature files for testing the Lambda functions using BDD-style scenarios. You can run these tests using a BDD testing framework like Behave.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request
