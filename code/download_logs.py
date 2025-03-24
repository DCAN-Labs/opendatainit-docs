import boto3
import os

s3 = boto3.client('s3')

bucket = 'bobsrepository-logs'

paginator = s3.get_paginator('list_objects_v2')
for page in paginator.paginate(Bucket=bucket):
    for obj in page.get('Contents', []):
        key = obj['Key']
        
        if not os.path.exists("./downloaded_logs"):
            os.makedirs("./downloaded_logs")
            
        local_path = os.path.join('./downloaded_logs', os.path.relpath(key))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        s3.download_file(bucket, key, local_path)
