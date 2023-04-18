# Question: Write a Python program to parse a log file and extract specific data, such as IP addresses and timestamps.
#
# Example log file
# 2023-04-18 10:05:30 - INFO - 192.168.1.100 - User logged in successfully
# 2023-04-18 10:08:45 - ERROR - 192.168.1.101 - Failed to load resource
# 2023-04-18 10:12:15 - INFO - 192.168.1.102 - User updated profile
import json
import re

string = """
# 2023-04-18 10:05:30 - INFO - 192.168.1.100 - User logged in successfully
# 2023-04-18 10:08:45 - ERROR - 192.168.1.101 - Failed to load resource
# 2023-04-18 10:12:15 - INFO - 192.168.1.102 - User updated profile
"""
pattern = r'\b([\d]{4}-[\d]{2}-[\d]{2})\b.*\b([\d]{2}:[\d]{2}:[\d]{2}).* \b([\.\d]+)\b'
match = re.findall(pattern, string)
data_logs = {}
for id, log_item in enumerate(match):
    data, time, ip_addr = log_item
    data_logs[f'log_{id}'] = {'data': data,
                'time': time,
                'ip_addr': ip_addr}
print(data_logs)

json_str_logs = json.dumps(data_logs, indent=4)
print(json_str_logs)


