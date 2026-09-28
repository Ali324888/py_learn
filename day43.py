from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    course: str

student = Student("Adil", 26, "Python")
print(student)


@dataclass
class Employee:
    name: str
    salary: int
    city: str = "Jaipur"

employee = Employee("Zee", 50000)

print(employee)


@dataclass
class Student:
    name: str
    marks: int

    def is_passing(self):
        return self.marks >= 40

student1 = Student("Adil", 75)
student2 = Student("Zee", 30)

print(student1.is_passing())
print(student2.is_passing())


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_price(self):
        return self.price * self.quantity

    def discount_price(self, percent):
        return self.price * self.quantity * (100 - percent)/100

product = Product("Laptop", 50000, 2)

print(product)
print(product.total_price())
print(product.discount_price(10))