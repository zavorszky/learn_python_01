# Project: 01
# File: 15_json.py
# Author: zavorszky@yahoo.com

import json

print("** 1 **")
jsonString1 = '{"name": "John", "age": 30, "city": "New York"}'

dictionaryObj1 = json.loads(jsonString1)

print(f'{dictionaryObj1["name"]} életkora {dictionaryObj1["age"]}.')
print(dictionaryObj1)

print("\n** 2 **")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("\n** 3 **")
jsonString3 = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

pyObj3 = json.dumps(jsonString3)

print(pyObj3)

print("\n** 3a **")
print(json.dumps(jsonString3, indent=4))

print("\n** 3b **")
print(json.dumps(jsonString3, indent=4, separators=(". ", " = ")))
