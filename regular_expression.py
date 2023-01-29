import re
text = '1230014'
match = re.findall(r"[^0][\d]*", text)
print(match)
