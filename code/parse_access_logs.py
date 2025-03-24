import os
import re
import argparse
from datetime import datetime
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

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
                    if log['operation'] == 'REST.GET.OBJECT' and log['http_status'] == '200':
                        log_time = datetime.strptime(log['datetime'], "%d/%b/%Y:%H:%M:%S %z")
                        log_entry = {
                            'date': log_time.date(),
                            'remote_ip': log['remote_ip'],
                            'operation': log['operation'],
                            'status': int(log['http_status'])
                        }
                        log_entries.append(log_entry)
                else:
                    print("No match found for line:", line)

# Create pandas DataFrame
df = pd.DataFrame(log_entries)

# Drop duplicates
df= df.drop_duplicates()
df.to_csv(f'{output_dir}/REST.GET.OBJECT_200.csv', index=False)

# Remove IP duplicates across time
df_unique= df.drop_duplicates('remote_ip')
df_unique.to_csv(f'{output_dir}/REST.GET.OBJECT_200_unique.csv', index=False)

# Grab period of time and total unique downloads
sorted_df = df_unique.sort_values(by='date')
first_date= sorted_df.iloc[0]['date']
last_date=sorted_df.iloc[-1]['date']

# Plot daily downloads
df['date'] = pd.to_datetime(df['date'])
downloads_per_week = df.groupby(pd.Grouper(key='date', freq='W')).size().reset_index(name='count')

# Plot line + dots
plt.figure(figsize=(10, 6))
plt.plot(downloads_per_week['date'], downloads_per_week['count'], marker='o', linestyle='-')

plt.title(f'Successful Downloads Per Week {first_date} to {last_date} \n Total # Unique Downloads: {len(sorted_df)}')
plt.xlabel('Week')
plt.ylabel('Download Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

fig_path = os.path.join(output_dir, 'downloads_over_time.png')
plt.savefig(fig_path)



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