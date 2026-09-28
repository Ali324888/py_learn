import json, requests

json_data = '{"name": "Zee", "age": 30, "city": "Kota"}'

data = json.loads(json_data)

print("Name: ", data["name"])
print("Age: ", data["age"])
print("City: ", data["city"])

student = {
    "name": "Adil",
    "age": 26,
    "course": "Python"
}

data = json.dumps(student, indent=4)

print(data)

student = {
    "name": "Adil",
    "age": 26,
    "marks": [80, 90, 75]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    user = json.load(file)

print("Name:", user["name"])
print("Age:", user["age"])

def save_users(filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

save_users("users.json")


with open("users.json", "r") as file:
    users = json.load(file)

for user in users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])