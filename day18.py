def hello():
    print("Hello Python")

hello()
hello()
hello()

def greet(name):
    print("Hello ", name)

greet("Zee")

def add(a,b):
    return a+b

result = add(10,20)

print(result)

def square(number):
    return number*number

print(square(5))

def check_number(number):
    if number > 0 :
        print("Positive")
    elif number < 0:
        print("Negative")
    elif number == 0:
        print("Zero")

check_number(10)
check_number(-5)
check_number(0)