import boto3
import os
import argparse

parser = argparse.ArgumentParser(description="Download AWS S3 access logs not already present in local directory.")
parser.add_argument("--bucket", type=str, required=True, help="Bucket name to download logs from")
args = parser.parse_args()
bucket = args.bucket

s3 = boto3.client('s3')

# Use enters AWS credentials
os.system('aws configure')

paginator = s3.get_paginator('list_objects_v2')

if not os.path.exists('./downloaded_logs'):
    os.makedirs('./downloaded_logs')

for page in paginator.paginate(Bucket=bucket):
    for obj in page.get('Contents', []):
        key = obj['Key']
        local_dir = os.path.join('./downloaded_logs', os.path.dirname(key))
        
        # Skip download if folder already exists
        if os.path.exists(local_dir):
            print(f"Skipping {key} - folder already exists.")
            continue

        # Create local folder
        os.makedirs(local_dir, exist_ok=True)
        local_path = os.path.join('./downloaded_logs', key)
        
        print(f"Downloading {key} to {local_path}")
        s3.download_file(bucket, key, local_path)