import time

def before(function):
    def wrapper():
        print("Before function")
        function()

    return wrapper

def after(function):
    def wrapper():
        function()
        print("After function")

    return wrapper



@before
@after
def hello():
    print("Hello Python")

hello()

def show_result(function):
    def wrapper(*args, **kwargs):
        result = function(*args,**kwargs)
        print("Result: ", result)
        return result
    return wrapper

@show_result
def add(a,b):
    return a+b

add(20, 30)

def timer(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print("Time taken: ", end-start,"seconds")
        return result
    return wrapper

@timer
def test():
    # time.sleep(5)
    print("Done")

test()


def log_function(function):
    def wrapper(*args, **kwargs):
        print("Calling: ", function.__name__)
        print("Finished: ", function.__name__)
        result = function(*args,**kwargs)
        return result
    return wrapper

@log_function
def greet(name):
    return "Hello " + name

result = greet("Zee")

print(result)

def check_permission(function):
    def wrapper(*args, **kwargs):
        if args[1]:
            result = function(*args, **kwargs)
            return result
        else:
            print("Permission denied")
    return wrapper


@check_permission
def delete_account(username, is_admin):
    print("Account deleted:", username)

delete_account("Zee", True)
delete_account("Tintin", False)