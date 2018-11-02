import boto3
from botocore.client import Config

BUCKET_NAME = 'dashrathpublicbucket'
FILE_NAME = 'demo.pdf'

s3 = boto3.resource('s3')

obj = s3.Object(BUCKET_NAME,FILE_NAME)

obj.delete()
print ("Done")