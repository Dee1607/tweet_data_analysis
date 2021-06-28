import boto3
import json
import pymysql


def connection():

    # These define the bucket and object to read
    bucketname = "tagsb00865413"
    file_to_read = "001ne.txt"

    # Create a file object using the bucket and object key.

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('tagsb00865413')

    fileobj = s3.Object(bucketname, file_to_read)
    key = fileobj.key
    body = fileobj.get()['Body'].read()
    content = body.decode('utf-8')

    json1_data = json.loads(content)

    connection = pymysql.connect(host = 'frequency-count-db.csogz3jhmpaf.us-east-1.rds.amazonaws.com',
    user = 'admin',
    password = 'Admin123',
    database = 'frequency-count-db')
    cur = connection.cursor()
    sql = "INSERT INTO `frequencyCount` (`NamedEntity`, `Frequency`) VALUES (%s, %s)"

    for key in json1_data['001ne'][0]:
        value = json1_data['001ne'][0][key]
        key =key.replace(",", "")
        print(key)
        print(value)
        cur.execute(sql, (key, value))
    connection.commit()
    cur.close()

connection()