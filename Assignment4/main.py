import boto3
import os
from botocore.exceptions import NoCredentialsError

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


path = '/Users/deeppatel/Desktop/A4_Serverless/file_mongo_tweets.txt'
upload_to_aws(path, 'twitterdatab00865413', 'file_mongo_tweets.txt')
