import boto3
import re
import os
import emoji as emoji
import nltk as nltk
from botocore.exceptions import NoCredentialsError
import json
from nltk.corpus import words


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


def read_file():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('twitterdatab00865413')
    tweets = ''
    for obj in bucket.objects.all():
        key = obj.key
        if key == 'file_mongo_tweets.txt':
            body = obj.get()['Body'].read()
            tweets = body.decode('utf-8')

    tweets.replace("RT", "").replace(":", "").lstrip()
    tweets.replace("\n", "")
    tweetList = tweets.split("@")
    # print(tweetList)

    cleanedTweets = []
    tweetData = ''
    for tweet in tweetList:
        tweet = re.sub("@[A-Za-z0-9]+", "", tweet)  # Remove @ sign
        tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet)  # Remove http links
        tweet = tweet.replace("RT", "").lstrip()  # Remove Re-Tweet's RT
        tweet = tweet.replace("#", "").replace("_", " ")  # Remove hashtag sign but keep the text
        tweet = " ".join(tweet.split())

        if tweet != '' and len(tweet) > 50:
            cleanedTweets.append(tweet)
            tweetData = tweetData + "\n" + tweet

    # s3 Client.put_object()
    client = boto3.client('s3')
    client.put_object(Body=tweetData, Bucket='twitterdatab00865413', Key='cleaned_tweets.txt')

    print_analysis()


def print_analysis():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('twitterdatab00865413')
    tweets = ''
    for obj in bucket.objects.all():
        key = obj.key
        if key == 'cleaned_tweets.txt':
            body = obj.get()['Body'].read()
            tweets = body.decode('utf-8')

    count = 0
    data = []
    tweetData = tweets.split("\n")
    for tweet in tweetData:
        if count < 10:
            data.append(tweet)
            count = count + 1

    print(data)

    client = boto3.client('comprehend', region_name='us-east-1')
    # Sentiments
    analysisData = ''
    for i in range(len(data)):
        d = data[i]

        if d != '':
            d = d.replace(",", "").lstrip()
            res = client.detect_sentiment(Text=d, LanguageCode='en')
            s = res['Sentiment']
            p = res['SentimentScore']['Positive']
            neg = res['SentimentScore']['Negative']
            neu = res['SentimentScore']['Neutral']
            mix = res['SentimentScore']['Mixed']

            analysisData = analysisData + '\n' + d + ',' + str(s) + ',' + str(p) + ',' + str(neg) + ',' + str(neu) + ',' + str(mix)

    print(analysisData)
    # s3 Client.put_object()
    client = boto3.client('s3')
    client.put_object(Body=analysisData, Bucket='twitterdatab00865413', Key='sentiment_analysis.csv')

    # count = 0
    # data = ''
    # tweetData = tweets.split("\n")
    # for tweet in tweetData:
    #     if count < 10:
    #         data = data + "\n" +tweet
    #         count = count + 1
    #
    # print(data)
    # sentiment = client.detect_sentiment(Text=data, LanguageCode='en')  # API call for sentiment analysis
    # sentRes = sentiment['Sentiment']  # Positive, Neutral, or Negative
    # sentScore = sentiment['SentimentScore']  # Percentage of Positive, Neutral, and Negative
    #
    # # Print the sentiment:
    # print('------- sentiment ---------')
    # print(sentRes)
    # print(sentScore)


read_file()
