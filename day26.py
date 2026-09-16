class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)


mobile1 = Mobile("Samsung", "Galaxy", 50000)
mobile2 = Mobile("Oppo", "Reno 15 mini", 65000)

print("Brand: ",mobile1.brand)
print("Model: ",mobile1.model)
print("Price: ",mobile1.price)
print("\n")

mobile2.show_details()

class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 

    def checkResult(self):
        if self.marks >= 40:
            print("Passed")
        else:
            print("Failed")

student1 = Student("anita", 60)
student2 = Student("sunita", 35)

student1.checkResult()
student2.checkResult()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Name: ",self.name)
        print("Balance: ",self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount


account1 = BankAccount("Zee", 10000)

account1.deposit(5000)
account1.withdraw(2000)
account1.show_balance()