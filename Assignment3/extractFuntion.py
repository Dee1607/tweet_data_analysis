import json

import boto3
from botocore.exceptions import NoCredentialsError

def extractFuntion():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('sampledatab00865413')
    content = ''
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
        content = body.decode('utf-8')

    print(content)
    words = content.split()

    namedEntities = {}
    for word in words:
        word = word.replace(".", "")
        word = word.replace(",", "")
        if word[0].isupper():
            if word in namedEntities:
                namedEntities[word] += 1
            else:
                namedEntities[word] = 1

    print(namedEntities)

    data = {}
    data["001ne"] = []
    data["001ne"].append(
        namedEntities
    )
    jsonData = json.dumps(data)

    print(jsonData)

    object = s3.Object('tagsb00865413', 'tags.txt')
    object.put(Body=str(jsonData))

extractFuntion()