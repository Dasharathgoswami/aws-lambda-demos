

#   Author: Dashrath Goswami
#   Date:   16th May 2020
#   Detail: to check status of rds instances using tags
#   Note:   Aurora databases are currently not supported for shutdown and startup methods.


import boto3

#aws iam user credentials
aws_key = ''
aws_secret = ''

#db tags 
Key = 'db-type'
Value = 'customer-replication'

client = boto3.client(
    'rds',
    aws_access_key_id = aws_key,
    aws_secret_access_key = aws_secret 
)
response = client.describe_db_instances()

for resp in response['DBInstances']:
   db_instance_arn = resp['DBInstanceArn']


   response = client.list_tags_for_resource(ResourceName=db_instance_arn)
   for tags in response['TagList']:
       if tags['Key'] == str(Key) and tags['Value'] == str(Value):
           status = resp['DBInstanceStatus']
           InstanceID = resp['DBInstanceIdentifier']
           print(InstanceID + " = " + status)
           
          