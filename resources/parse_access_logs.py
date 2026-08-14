import os
import re
import argparse
from datetime import datetime
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

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
                            'status': int(log['http_status']),
                            'bytes': log['bytes_sent'],                           
                            'user_agent': log['user_agent'],
                            'object_size': log['object_size']
                        }
                        log_entries.append(log_entry)
                else:
                    print("No match found for line:", line)

# Create pandas DataFrame
df = pd.DataFrame(log_entries)
df.to_csv(f'{output_dir}/parsed_output.csv', index=False)

# Remove rows with missing object size or bytes sent
df = df[
    (df['object_size'] != '-') &
    (df['bytes'] != '-')  
]

# Drop duplicates & remove IP duplicates across time (note that this will remove downloads from the same IP on different days)
df= df.drop_duplicates()
df_unique= df.drop_duplicates('remote_ip')

# Filter likely bots
bot_keywords = ['bot', 'crawl']
df_bots_filt = df_unique[~df_unique['user_agent'].str.lower().str.contains('|'.join(bot_keywords))]

# Grab period of time and total unique downloads
sorted_df = df_bots_filt.sort_values(by='date')
first_date= sorted_df.iloc[0]['date']
last_date=sorted_df.iloc[-1]['date']

# Save filtered data
df_unique.to_csv(f'{output_dir}/parsed_output_filt.csv', index=False)

# Plot daily downloads
df_bots_filt['date'] = pd.to_datetime(df_bots_filt['date'])
downloads_per_week = df_bots_filt.groupby(pd.Grouper(key='date', freq='W')).size().reset_index(name='count')

# Plot line + dots
plt.figure(figsize=(10, 6))
plt.plot(downloads_per_week['date'], downloads_per_week['count'], marker='o', linestyle='-')

plt.title(f'Successful Downloads Per Week By Unique Users {first_date} to {last_date} \n Total # Downloads: {len(sorted_df)}')
plt.xlabel('Date')
plt.ylabel('Download Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True)) # Force y-axis to be integers
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