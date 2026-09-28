import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

data = response.json()

print(response)
print(response.status_code)
print(response.ok)

print(data)
print(type(data))

print(data["userId"])
print(data["id"])
print(data["title"])
print(data["completed"])

response2 = requests.get("https://jsonplaceholder.typicode.com/todos/5")
data2 = response2.json()

print("ID: ",data2["id"])
print("Title: ",data2["title"])
print("Completed",data2["completed"])

def get_todo(todo_id):
    api_url = "https://jsonplaceholder.typicode.com/todos/"+todo_id
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print("ID: ",data["id"])
        print("Title: ",data["title"])
        print("Completed",data["completed"])
    else:
        print("Todo not found")


get_todo("10")