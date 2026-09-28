from functools import wraps

def calculate(operation, *numbers):
    if operation == "add":
        total = 0
        for number in numbers:
            total += number
        print(total)
    elif operation == "multiply":
        total = 1
        for number in numbers:
            total *=number
        print(total)
    elif operation == "average":
        total = 0
        for number in numbers:
            total += number
        average = total/ len(numbers)
        print(average)


calculate("add", 10, 20, 30)
calculate("multiply", 2, 3, 4)
calculate("average", 10, 20, 30)

def create_profile(**details):
    print("Name: ", details.get("name"))
    print("Age: ", details.get("age"))
    print("City: ", details.get("city"))

create_profile(
    name="Zee",
    age=30,
    city="Kota"
)

def logger(function):
    def wrapper(*args, **kwargs):
        print(function.__name__)
        print(*args)
        result = function(*args,**kwargs)
        return result
    return wrapper

@logger
def multiply(a,b):
    return a*b

result = multiply(5,10)
print(result)

def check_permission(function):
    def wrapper(*args, **kwargs):
        if kwargs.get("is_admin"):
            result = function(*args, **kwargs)
            return result
        else:
            print("Permission denied")

    return wrapper

@check_permission
def view_salary(name, is_admin=False):
    print("Salary of", name, "is ₹50,000")

view_salary(name="Zee", is_admin=True)

view_salary(name="Tintin", is_admin=False)


def logger(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print("Calling: ", function.__name__)
        function(*args, **kwargs)
        print("Finished: ", function.__name__)
    return wrapper

def check_permission(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if kwargs.get("is_admin"):
            result = function(*args,**kwargs)
            return result
        else:
            print("Permission denied")
    return wrapper

@logger
@check_permission
def manage_user(action, username, is_admin=False):
    if action == "add":
        print("User added: ", username)
    elif action == "delete":
        print("User deleted: ", username)
    else:
        print("Invalid action")

manage_user(
    "add",
    "Zee",
    is_admin=True
)

manage_user(
    "delete",
    "Zee",
    is_admin=True
)

manage_user(
    "delete",
    "Tintin",
    is_admin=False
)

manage_user(
    "hello",
    "Zee",
    is_admin=True
)