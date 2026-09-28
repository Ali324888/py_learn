class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


book = Book("Python Basics", "Adil")
print(book)

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

playlist = Playlist(["Song 1", "Song 2", "Song 3", "Song 4"])
print(len(playlist))

class Number: 
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

num1 = Number(10)
num2 = Number(20)

print(num1 + num2)

class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

student1 = Student("Adil", 26)
student2 = Student("Adil", 26)
student3 = Student("Zee", 30)

print(student1 == student2)
print(student1 == student3)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Holder: {self.name}, Balance: {self.balance}"

    def __eq__(self, other):
        return self.name == other.name and self.balance == other.balance

    def __add__(self, other):
        return self.balance + other.balance

account = BankAccount("Zee", 10000)

print(account)

account1 = BankAccount("Zee", 10000)
account2 = BankAccount("Zee", 10000)
account3 = BankAccount("Adil", 5000)

print(account1 == account2)
print(account1 == account3)

print(account1 + account3)