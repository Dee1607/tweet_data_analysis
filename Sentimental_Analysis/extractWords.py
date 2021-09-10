import boto3
from botocore.exceptions import NoCredentialsError
import csv

from Levenshtein import distance as lev
import spacy
sp = spacy.load('en_core_web_sm')


def remove_mystopwords(sentence):
    print(sentence)
    tokens = sentence.split(" ")
    my_stopwords = sp.Defaults.stop_words
    my_stopwords.add(".")
    my_stopwords.add(",")
    my_stopwords.add(":")
    my_stopwords.add("/")
    my_stopwords.add("\"")
    my_stopwords.add("-")
    my_stopwords.add("(")
    my_stopwords.add(")")
    my_stopwords.add("{")
    my_stopwords.add("}")
    my_stopwords.add("[")
    my_stopwords.add("]")

    tokens_filtered= [word for word in tokens if not word in my_stopwords]
    return (" ").join(tokens_filtered)


def read_file():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('sourcedatab00865413')
    final_data = []
    for obj in bucket.objects.all():
        key = obj.key
        if int(key.split(".")[0]) >= 300 and int(key.split(".")[0]) <= 401:
            body = obj.get()['Body'].read()
            content = body.decode('utf-8')
            content = content.replace(',', '')
            content = content.replace('.', '')
            content = content.replace(':', '')
            content = content.replace('-', '')
            content = content.replace('"', '')
            content = content.replace('{', '')
            content = content.replace('}', '')
            content = content.replace('(', '')
            content = content.replace(')', '')
            content = content.replace('[', '')
            content = content.replace(']', '')

            content = remove_mystopwords(content)
            content = content.split(" ")
            final_data = final_data + content

    create_test_data(final_data)


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


def create_train_data(data):
    print("Creating Train Dataset...")

    with open('trainVector.csv', mode='w') as csv_file:
        fieldnames = ['Current_Word', 'Next_Word', 'Levenshtein_distance']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for word in data:
            next_word_index = (data.index(word) + 1)
            if next_word_index < len(data):
                next_word = data[next_word_index]
                writer.writerow({'Current_Word': word, 'Next_Word': next_word,
                                 'Levenshtein_distance': lev(word, next_word)})

        print("Train Dataset Created Successfully!!")
        upload_to_aws('trainVector.csv', 'traindatab00865413', 'trainVector.csv')


def create_test_data(data):
    print("Creating Train Dataset...")

    with open('testVector.csv', mode='w') as csv_file:
        fieldnames = ['Current_Word', 'Next_Word', 'Levenshtein_distance']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for word in data:
            next_word_index = (data.index(word) + 1)
            if next_word_index < len(data):
                next_word = data[next_word_index]
                writer.writerow({'Current_Word': word, 'Next_Word': next_word,
                                 'Levenshtein_distance': lev(word, next_word)})

        print("Test Dataset Created Successfully!!")
        upload_to_aws('testVector.csv', 'testdatab00865413', 'testVector.csv')


read_file()
