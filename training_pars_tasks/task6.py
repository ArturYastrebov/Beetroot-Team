# 6. Question: Implement a Python function to extract data from a web API response, such as JSON or XML, and store it in a structured format for further processing.
import json

json_data = '{"person": {"name": "John", "age": 30, "city": "New York"}}'


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"{self.name} ({self.age}, {self.city})"

    def to_dict(self):
        return {"name": self.name, "age": self.age, "city": self.city}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["city"])

# Deserialize JSON string back to object
data = json.loads(json_data)
person = Person.from_dict(data['person'])
print(person)
