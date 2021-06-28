import boto3
import wordcounter
from botocore.exceptions import NoCredentialsError

# s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)


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

uploaded = upload_to_aws('/Users/deeppatel/Desktop/CSCI_5410_Assignment-3/tech/014.txt', 'sampledatab00865413', '014.txt')

# def read_file():
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket('sampledatab00865413')
#     content = ''
#     for obj in bucket.objects.all():
#         key = obj.key
#         body = obj.get()['Body'].read()
#         content = body.decode('utf-8')
#
#     print(content)
#
#     words = content.split()
#
#     namedEntities = {}
#     for word in words:
#         word = word.replace(".", "")
#         word = word.replace(",", "")
#
#         if word[0].isupper():
#             if word in namedEntities:
#                 namedEntities[word] += 1
#             else:
#                 namedEntities[word] = 1
#
#     print(namedEntities)
#
#     data = {}
#     data['001ne'] = []
#     data['001ne'].append(
#         str(namedEntities)
#     )
#     print(data)
#
#     object = s3.Object('tagsb00865413', '001ne.txt')
#     object.put(Body=str(data))
#
# read_file()

# upload_to_aws(str(data), 'tagsb00865413', '001ne.txt')


