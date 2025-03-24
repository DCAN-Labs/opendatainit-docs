import os
import re
import argparse
from datetime import datetime
from collections import defaultdict
import pandas as pd

log_pattern = re.compile(r'''
    (?P<bucket_owner>\S+) \s+
    (?P<bucket>\S+) \s+
    \[(?P<datetime>[^\]]+)\] \s+
    (?P<remote_ip>\S+) \s+
    (?P<requester>\S+) \s+
    (?P<request_id>\S+) \s+
    (?P<operation>\S+) \s+
    (?P<key>\S+) \s+
    "(?P<request_uri>[^"]+)" \s+
    (?P<http_status>\d+) \s+
    (?P<error_code>\S+) \s+
    (?P<bytes_sent>\S+) \s+
    (?P<object_size>\S+) \s+
    (?P<total_time>\S+) \s+
    (?P<turn_around_time>\S+) \s+
    "(?P<referrer>[^"]*)" \s+
    "(?P<user_agent>[^"]*)" \s+
    (?P<version_id>\S+) \s+
    (?P<host_id>\S+) \s+
    (?P<signature_version>\S+) \s+
    (?P<cipher>\S+) \s+
    (?P<host>\S+) \s+
    (?P<tls_version>\S+) \s+
    (?P<access_point_arn>\S+) \s+
    (?P<acl_required>\S+)
''', re.VERBOSE)

parser = argparse.ArgumentParser(description="Parse AWS S3 access logs for views and unique downloads.")
parser.add_argument("--log-dir", type=str, required=True, help="Path to the root log directory")
args = parser.parse_args()
log_dir = args.log_dir

downloads = defaultdict(lambda: defaultdict(lambda: {'views': 0, 'unique_ips': set()}))
log_entries = []

# Create directory for parsed logs
output_dir = 'parsed_logs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for root, _, files in os.walk(log_dir):
    for file in files:
        filepath = os.path.join(root, file)
        with open(filepath) as f:
            for line in f:
                match = log_pattern.match(line)
                if match:
                    log = match.groupdict()
                    #if log['operation'] == 'REST.GET.OBJECT' and log['http_status'] == '200':
                    if log['operation'] == 'REST.GET.OBJECT':
                        log_time = datetime.strptime(log['datetime'], "%d/%b/%Y:%H:%M:%S %z")
                        log_entry = {
                            'date': log_time.date(),
                            'remote_ip': log['remote_ip'],
                            'operation': log['operation'],
                            'status': int(log['http_status']),
                        }
                        log_entries.append(log_entry)
                else:
                    print("No match found for line:", line)

# Create pandas DataFrame
df = pd.DataFrame(log_entries)

# Drop duplicates
df_unique = df.drop_duplicates()
df_unique.to_csv(f'{output_dir}/full.csv', index=False)

df_successful_downloads = df_unique[df_unique['status'] == 200]
df_successful_downloads= df_successful_downloads.drop(['operation', 'status'], axis=1)
df_successful_downloads.to_csv(f'{output_dir}/REST.GET.OBJECT_200.csv', index=False)

# Remove IP duplicates across time
df_successful_downloads_unique= df_successful_downloads.drop_duplicates('remote_ip')
df_successful_downloads_unique.to_csv(f'{output_dir}/REST.GET.OBJECT_200_unique.csv', index=False)

# Grab period of time and total unique downloads
sorted_df = df_successful_downloads_unique.sort_values(by='date')
first_date= sorted_df.iloc[0]['date']
last_date=sorted_df.iloc[-1]['date']

print(f"From the period of {first_date} to {last_date}, there were {len(sorted_df)} downloads by unique users.")



'''
operations:
Operation	Description
REST.GET.OBJECT	Download an object (GET)
REST.PUT.OBJECT	Upload an object
REST.DELETE.OBJECT	Delete an object
REST.HEAD.OBJECT	Get object metadata
REST.GET.BUCKET	List bucket contents
REST.HEAD.BUCKET	Check if bucket exists
WEBSITE.GET.OBJECT	Request via S3 static website endpoint


Errors:
301 - moved permanently
401 - invalid credentials
404 - object not found
'''