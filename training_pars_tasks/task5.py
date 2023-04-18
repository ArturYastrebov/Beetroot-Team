# 5. Question: Write a Python program to parse a complex data file in a custom format and extract specific data fields using string manipulation and pattern matching.
#
# OUT format — json file

string = """
#Person1
Name: John Doe
Age: 30
City: New York
#Person2
Name: Alice Johnson
Age: 25
City: Los Angeles
"""

import json
import re
#
pattern = r'#([\w]+)\sName: ([\w]+ [\w]+).*\sAge: ([\d]+).*\sCity: ([\w ]+)\s'
match = re.findall(pattern, string)
print(match)
contacts = {}
for item in match:
    id, name, age, city = item
    contacts[id] = {'name': name,
                'age': age,
                'city': city}

print(contacts)

json_contacts = json.dumps(contacts, indent=4)
print(json_contacts)
