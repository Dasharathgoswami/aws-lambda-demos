import boto3
import json

dynamo = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):


    dynamo.put_item(TableName='SchedulerConfig', Item={
        
  "type": {
    "S": "schedule"
  },
  "name": {
    "S": "nonbusiness-hours"
  },
  "use_maintenance_window": {
    "BOOL": False
  },
  "stop_new_instances": {
    "BOOL": True
  },
  "use_metrics": {
    "BOOL": False
  },
  "timezone": {
    "S": "America/New_York"
  },
  "hibernate": {
    "BOOL": False
  },
  "enforced": {
    "BOOL": False
  },
  "retain_running": {
    "BOOL": False
  },
  "periods": {
    "SS": [
      "nonbusiness-hours"
    ]
  }
}
)

    dynamo.put_item(TableName='SchedulerConfig', Item={
        
     "type": {
     "S": "period"
     },
    "name": {
    "S": "nonbusiness-hours"
    },
    "begintime": {
    "S": "07:00"
    },
    "endtime": {
    "S": "15:00"
    },
     "weekdays": {
      "SS": [
        "mon-fri"
      ]
     }
     }
    )

    
    table = dynamodb.Table('SchedulerConfig')
    response = table.scan()
    data = response['Items']
    

    return json.dumps(data, default=str)
