def show_name():
    name="Zee"
    print(name)

show_name()

def introduce(name,age,city):
    print("Name: ", name)
    print("Age: ", age)
    print("City: ", city)

introduce("Zee",25,"Delhi")

def greet(name="Greet"):
    print("Hello ", name)

greet()
greet("Zee")

def multiply(a,b):
    return a*b 

print(multiply(3,4))
print(multiply(13,14))

def calculate_bill(price, quantity, discount=0):
    total = price*quantity
    discount_amout = total*discount/100
    final_price = total - discount_amout
    return final_price

print(calculate_bill(1000, 2, 10))
print(calculate_bill(500, 2))