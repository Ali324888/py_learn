import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

def add_student(name,age,course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    connection.commit()

def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def get_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    return cursor.fetchone()

def update_course(student_id, new_course):
    cursor.execute("UPDATE students SET course= ? WHERE id=?", (new_course, student_id))
    connection.commit()

def delete_course(student_id):
    cursor.execute("DELETE FROM students WHERE id= ?", (student_id,))
    connection.commit()



# student = get_student(2)
# print(student)

# update_course(2, "Django")

while True:

    print("1. Add Student")
    print("2. Show Students")
    print("3. Find Student")
    print("4. Update Course")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        course = input("Enter student course: ")
        add_student(name,age,course)
        print("Student added successfully")
    elif choice == "2":
        students = get_students()
        for student in students:
            print(student)
    elif choice == "3":
        student_id = int(input("Please enter student id: "))
        student = get_student(student_id)
        print("Student: ", student)
    elif choice == "4":
        student_id = int(input("Please enter student id: "))
        new_course = input("Please enter student course: ")
        update_course(student_id, new_course)
        print("Course updated successfully")
    elif choice == "5":
        student_id = int(input("Please enter student id: "))
        delete_course(student_id)
        print("Course deleted")
    else:
        break
