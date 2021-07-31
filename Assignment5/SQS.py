# -*- coding: utf-8 -*-


import boto3
import time
import random

client = boto3.resource('sqs', region_name='us-east-1')

Queue = client.get_queue_by_name(QueueName='assignment5B00863421')
message = ['rose ordered','Lily only 2 left', 'sunflower are not in stock']
size = ['L', 'M', 'S']
while True:
	message = (random.choice(message))
    size = random.choice(size)
    data = message + " " + size
    response = queue.send_message(MessageBody= data)

