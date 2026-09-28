# class Animal:

#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def sound(self):
#         print("Dog is barking")

# dog = Dog()

# dog.eat()
# dog.sound()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_student(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Course: ", self.course)

student = Student("Adil", 26, "Node.js front to back")

student.show_student()

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog says Woof")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

cat = Cat()
dog = Dog()

dog.sound()
cat.sound()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

bank_account = BankAccount("Adil", 10000)
bank_account.deposit(2000)
bank_account.withdraw(3000)
bank_account.show_balance()

class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def show_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        print("Interest: ", interest_amount)

account = SavingsAccount("Zee", 10000, 5)
account.show_interest()
