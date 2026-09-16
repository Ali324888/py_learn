def decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("after function")

    return wrapper()

@decorator
def hello():
    print("Hello Python")

def decorating(function):
    def wrapper(*args, **kwargs):
        print("Calculating...")
        result = function(*args, **kwargs)
        return result
    return wrapper

@decorating
def add(a,b):
    return a+b

result = add(15,63)

print(result)

def sum(numbers):
    total=0
    for number in numbers:
        total += number

    return total
    

@decorating
def total(*numbers):
    return sum(numbers)

result = total(10, 20, 30, 40)
print(result)

def log_function(function):
    def wrapper(*args, **kwargs):
        print("Calling function: ",function.__name__ )
        function(*args, **kwargs)
        print("Function finished: ", function.__name__)

    return wrapper

@log_function
def greet(name):
    print("Hello", name)

greet("Adil")


def show_result(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper

@show_result
def multiply(a, b):
    return a * b

res = multiply(5,10)

print("Result: ", res)