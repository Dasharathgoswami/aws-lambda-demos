import boto3
import json


client = boto3.client('sns')
ec2 = boto3.resource('ec2')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    filter=[
            {
                'Name':'tag:Schedule',
                'Values':['business-hours']
            }
        ]
 
    instances = ec2.instances.filter(Filters=filter)

    table = dynamodb.Table('SchedulerState')
    response = table.scan()
    data = response['Items']

    for instance in instances:
        message = 'Please Check Your EC2 Instance State : \n' + str(data)
       
    topic_arn = 'arn:aws:sns:us-east-1:411161093658:Scheduler'
    client.publish(TopicArn=topic_arn,Message=message)
    
    return(data)
