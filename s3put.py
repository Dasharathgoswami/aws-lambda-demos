import boto3
from botocore.client import Config

BUCKET_NAME = 'dashrathpublicbucket'

data = open('demo.pdf', 'rb')

s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).put_object(Key='demo.pdf', Body=data)

print ("Done")