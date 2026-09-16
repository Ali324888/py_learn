def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total = total+number

    return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))

def student_marks(name, *marks):
    print("Name: ",name)
    print("Marks: ",marks)


student_marks("Zee", 80, 90, 75)

def show_profile(**details):
    print("Name: ", details['name'])
    print("Age: ", details['age'])
    print("City: ", details['city'])

show_profile(name="Zee", age=30, city="Jaipur")

def student(name, *marks, **details):
    print("Name: ",name)
    print("Marks: ",marks)
    print("Other Details: ",details)


student("Zee", 80, 90, 85, city="Jaipur", course="Python")