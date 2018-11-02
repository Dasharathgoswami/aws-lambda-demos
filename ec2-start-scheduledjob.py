#author : Dashrath Goswami
#This function use in lambda to start ec2 instances with specific tags at specific time 
#Use trigger cloudwatch event create rule using cron fromat expression for specific time
#give lambda function access ec2 start and ec2 describe
import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    filter=[
            {
                'Name':'tag:name',
                'Values':['prod']
            }
        ]
 
 	instances = ec2.instances.filter(Filters=filter)
    for instance in instances:
      instance.start()