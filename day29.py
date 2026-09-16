import json

def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


students = load_students()

def add_student():
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Please enter valid values")
        return

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    save_students()
    print("Student data added successfully!")

def view_students():
    if len(students) == 0:
        print("No student found!")
        return

    for student in students:
        print("--------------------")
        print("Name: ", student["name"])
        print("Age: ", student["age"])
        print("Marks: ", student["marks"])


def search_student():
    name = input("Please enter student's name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found!")
            print("Name: ", student["name"])
            print("Age: ", student["age"])
            print("Marks: ", student["marks"])
            return
    print("Student not found!")

def delete_student():
    name = input("Please enter student's name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return
    print("Student not found!")


while True:

    print("\n====Student management system====")
    print("1.Add student")
    print("2.View students")
    print("3.Search student")
    print("4.Delete student")
    print("5.Exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
