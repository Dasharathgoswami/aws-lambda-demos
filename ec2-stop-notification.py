#author : Dashrath Goswami
#This function use in lambda to trigger sns topic to notify user that instance is stopped or started
#Use trigger cloudwatch events via instance status
#give lambda function access of sns and cloudwatch log 
#rename topic arn and message as desired.
import boto3

client = boto3.client('sns')
def lambda_handler(event, context):
    topic_arn = 'arn:aws:sns:us-east-1:427413154210:ec2alert'
    message = 'prod server is sttoped.'
    client.publish(TopicArn=topic_arn,Message=message)
   
  
