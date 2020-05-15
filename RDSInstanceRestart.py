# this script will restart rds instance.
# you can modifie to start and stop also use cloudwatch event to start and stop on scheduler.
# detailed tutorial on this link : https://dzone.com/articles/create-an-aws-lambda-function-to-stop-and-start-an
import sys
import botocore
import boto3
from botocore.exceptions import ClientError
def lambda_handler(event, context):
    rds = boto3.client('rds')
    lambdaFunc = boto3.client('lambda')
    print 'Trying to get Environment variable'
    try:
        funcResponse = lambdaFunc.get_function_configuration(
            FunctionName='RDSInstanceStop'
        )
        DBinstance = funcResponse['Environment']['Variables']['DBInstanceName']
        print 'Restarting RDS service for DBInstance : ' + DBinstance
    except ClientError as e:
        print(e)    
    try:
        response = rds.reboot_db_instance(
            DBInstanceIdentifier=DBinstance
        )
        print 'Success :: ' 
        return response
    except ClientError as e:
        print(e)    
    return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complete output"
    }
