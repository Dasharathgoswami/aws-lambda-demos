import boto3
from botocore.client import Config

BUCKET_NAME = 'dashrathpublicbucket'
FILE_NAME = 'demo.pdf'

data = open('demo.pdf', 'rb')

s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).download_file(FILE_NAME,'download.pdf');

print ("Done")
#data = s3.Bucket(BUCKET_NAME).objects.all()
#
#for files in data:
#	print ('Filename:')
#	print (files.key)