# 6. Question: Implement a Python function to extract data from a web API response, such as JSON or XML, and store it in a structured format for further processing.
import json

json_data = '{"person": {"name": "John", "age": 30, "city": "New York"}}'
json_to_dict = json.loads(json_data)
print(json_to_dict)
print(json_to_dict['person']['name'])
print(json_to_dict['person']['age'])
print(json_to_dict['person']['city'])
