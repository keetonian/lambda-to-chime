# Lambda to Chime

This serverless app posts messages to an AWS Chime webhook.

## App Architecture

![App Architecture](https://github.com/keetonian/lambda-to-chime/raw/master/images/lambda-to-chime.png)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository]() and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

### Chime Url
To get a webhook URL for this application:
* Navigate to Settings -> Manage webhooks
* Select "Add Webhooks"
* Name your webhook (this will be the display name in the chat room)
* Copy the Url and paste it into the template parameter

## App Parameters

1. `ChimeUrl` (required) - Webhook URL for integration with Chime
1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO

## App Outputs

1. `LogsToChimeName` - Lambda function name.
1. `LogsToChimeArn` - Lambda function ARN.

## License Summary

This code is made available under the MIT license. See the LICENSE file.