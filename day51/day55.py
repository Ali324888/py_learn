import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

def add_student(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    connection.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

add_student("Adil", 26, "Python")
add_student("Zee", 30, "Python")
add_student("Rahul", 25, "Java")
add_student("kiti", 28, "cobal")

cursor.execute("SELECT * FROM students")



students = cursor.fetchall()

for student in students:
    print(student)

print("database connected")

connection.close()