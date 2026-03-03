import json

# Example 1

json_string = '{"name": "NurSat", "age": 17}'
data = json.loads(json_string)

print(data["name"])
print(data["age"])

# Example 2

person = {
    "name": "Ali",
    "age": 18
}

json_data = json.dumps(person, indent=4)
print(json_data)

# Example 3

with open("data.json", "w") as file:
    json.dump(person, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded from file:", loaded_data)