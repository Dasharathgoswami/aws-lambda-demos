#author : Dashrath Goswami
#This function use in lambda to trigger sns topic to notify user that instance is stopped or started
#also it give public ip of that instance in sns.
#Use trigger cloudwatch events via instance status
#give lambda function access of sns and cloudwatch log ,ec2 describe
#rename topic arn and message as desired.
import boto3
import json
client = boto3.client('sns')
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    filter=[
            {
                'Name':'tag:Name',
                'Values':['phplist']
            }
        ]
 
    instances = ec2.instances.filter(Filters=filter)

    for instance in instances:
        message = 'Your Aws EC2 Instance is Started And public Ip is : ' + instance.public_ip_address
       
    topic_arn = 'arn:aws:sns:us-east-1:427413154210:ec2alert_start'
    client.publish(TopicArn=topic_arn,Message=message)
   