# Question: Write a Python program to parse a formatted text file and extract relevant data, such as names, addresses, and phone numbers, using regular expressions.
# OUT format — json file
# Example formatted text file:

string = """
Name: John Doe
Age: 30
Address: 1234 Main St, Apt 567
Phone: (555) 123-4567

Name: Alice Johnson
Age: 25
Address: 5678 Elm St, Apt 890
Phone: (555) 987-6543
"""

import json
import re

pattern = r'Name: ([\w]+ [\w]+).*\sAge: ([\d]+).*\sAddress: ([\w\d,\s]+).*\sPhone: (\(\d{3}\) \d{3}-\d{4})'
match = re.findall(pattern, string)
print(match)
contacts = {}
for item in match:
    name, age, address, phone = item
    contacts[name] = {'age': age,
                'address': address,
                'phone': phone}

print(contacts)

json_contacts = json.dumps(contacts, indent=4)
print(json_contacts)
