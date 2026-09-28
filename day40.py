class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print("School: ", cls.school)

Student.show_school()


class Calculator: 

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def subtract(a,b):
        return a-b

    @staticmethod
    def multiply(a,b):
        return a*b

print(Calculator.add(10, 20))
print(Calculator.subtract(20, 5))
print(Calculator.multiply(5, 4))

class Student:
    school = "Abc School"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_student(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

    @classmethod
    def show_school(cls):
        print("School Name: ", cls.school)

    @staticmethod
    def is_adult(age):
        return age >= 18

student = Student("Zee", 30)

student.show_student()
Student.show_school()

print(Student.is_adult(30))
print(Student.is_adult(15))



class Employee: 
    company = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_employee(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)

    @classmethod
    def show_company(cls):
        print("Company: ", cls.company)

    @staticmethod
    def is_valid_salary(salary):
        return salary >= 10000


employee = Employee("Adil", 50000)

employee.show_employee()
Employee.show_company()

print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(5000))
