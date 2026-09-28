class BankAccount:
    def __init__(self, __balance):
        self.__balance = __balance

    def deposit(self, amount):
        if amount < 0:
            print("Invalid amount")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficiant balance")
        else:
            self.__balance -= amount

    def show_balance(self):
        print("Balance: ",self.__balance)


account = BankAccount(10000)

account.deposit(2000)
account.withdraw(3000)
account.show_balance()

class Student:
    def __init__(self, __marks):
        self.__marks = __marks

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            print("Invalid Marks")
        else: 
            self.__marks = marks

    def show_marks(self):
        print("Marks: ", self.__marks)

student = Student(50)
student.set_marks(60)
student.show_marks()

class Dog:
    def sound(self):
        print("Woof")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

class Payment:
    def pay(self, amount):
        print("Processing payment:", amount)

class UPI(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class Card(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Card")


class Cash(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Cash")

payments = [
    UPI(),
    Card(),
    Cash()
]

for payment in payments:
    payment.pay(1000)