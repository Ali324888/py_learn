import requests

api_url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(api_url)

data = response.json()

print("Status:", response.status_code)
print("Number of users:", len(data))

for user in data:
    print("Name: ", user["name"])
    print("Email: ", user["email"])


def get_users():
    api_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch users")
        return []


def find_user_by_id(user_id):
    api_url = "https://jsonplaceholder.typicode.com/users/"+str(user_id)
    
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data["id"] == user_id:
            print("Name: ", data["name"])
            print("Email: ", data["email"])
    else:
        print("User not found")

def find_user_by_name(name):
    api_url = "https://jsonplaceholder.typicode.com/users?name="+name
    
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        for user in data:
            if user["name"].lower() == name.lower():
                print("Name: ", user["name"])
                print("Email: ", user["email"])
    else:
        print("User not found")

print("-"*30)
find_user_by_id(3)
print("*"*30)
find_user_by_name("Leanne Graham")