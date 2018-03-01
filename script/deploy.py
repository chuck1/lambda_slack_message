import sys
import os
import boto3

def upload(resource, bucket, filename, name):
    print('uploading:', filename)

    res = resource.Object(bucket, name).put(Body=open(filename, 'rb'))

if __name__ == '__main__':

    resource = boto3.resource('s3')
    bucket = "lambda-slack-message"

    filename = sys.argv[1]
    
    upload(resource, bucket, filename, 'code.zip')

    client = boto3.client('lambda')

    response = client.update_function_code(
            FunctionName='SlackMessage',
            S3Bucket=bucket,
            S3Key='code.zip')

    print(response)

