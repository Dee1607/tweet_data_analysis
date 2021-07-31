import json 
import boto3 

def lambda_handler(event, context): 
    client = boto3.client('sqs', region_name='us-east-1', aws_access_key_id="ASIAWXU5W2ERGMUOD47E",
	aws_secret_access_key="VMIkbzpv7v60iLkSdLK1S2k1Y80zHww4tPtbxR3O"
	aws_session_token="FwoGZXIvYXdzELz//////////wEaDPw8Pbl38wl9u/gRfyK/Act+BdeQB9W43bO2m+bjKp5Gh95aWL9yCIol/I0lc6FegsjzvEW8nrP0vThrey3xtJWRSvbpKfTehr9ogXk1Ka+XZ2292btxFbXKuh0AeZFR2xgKWXmrj7pIV4rJJlfb/CkMtf+h9QtTTBGJlNf+CpTBeDlrmBTM8mgqYNY6NQ+PbYwqlquBQjkEdfcaLcxC1t8wLU385Zp6mSPOOkVWV4lOMoqdWy8JkHdyuu88X1SoOlWNqo3gZYxgEc5m5GHWKO/tkogGMi06dxrUOXeVtTRhXccfgOVyCSwlYU9ipaGnDtUOgC/7mnPq+oL21F4fRYaQwj0=")
    
    response = client.receive_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/211131213234/FlowerDelieryQueue')
    m = response['Messages'][0] 
    messageData = m['Body'] 
    
    snsClient = boto3.client('sns') 
    snsClient.publish(TopicArn = 'arn:aws:sns:us-east-1:34455147366:mailService', m = 'order ready' + messageData, Subject = 'Order Ready') 
    Order_handle = m['ReceiptHandle'] 
    res = client.delete_message( QueueUrl="https://sqs.us-east-1.amazonaws.com/211131213234/FlowerDelieryQueue", ReceiptHandle=Order_handle)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello!')
    }
