import datetime, random

date = datetime.date(2026,9,10)

print("Today: ",date)

current_date = datetime.date.today()

print("Year: ",current_date.year)
print("Month: ",current_date.month)
print("Day: ",current_date.day)

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

random_fruits = random.choice(fruits)
print(random_fruits)

birth_year = int(input("Please enter your birth year: "))

current_year = datetime.date.today().year

age = current_year - birth_year

print("Your Age is: ", age)

name = input("Enter your name: ")

random_number = random.randint(1,100)

print("Hello ", name)
print("Your lucky number is: ", random_number)

dice_number = random.randint(1,6)
print("Roling dice...")
print("You got: ",dice_number)