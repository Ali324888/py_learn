student = {
    "name": "Zee",
    "age": 30,
    "city": "Jaipur"
}

print(student)
print(student["age"])
print(student["name"])
print(student["city"])

student["city"] = "Kota"

print(student)

student["course"] = "Python"

print(student)
print(student.keys())
print(student.values())
print(student.items())

print(student.get('name'))
print(student.get('age'))
print(student.get('phone'))

product = {
    "name": "Laptop",
    "price": 50000,
    "quantity": 2
}

print(product.get('name'))
print(product.get('price'))
print(product.get('quantity'))

product["price"] = 55000
product["brand"] = "Dell"

print(product)