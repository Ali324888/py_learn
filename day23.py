try:
    age = int(input("Enter the Age: "))
    print("Your age is: ",age)

except ValueError:
    print("Please enter valid age!")

try:
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))

    division = number1/number2

    print(division)

except ValueError:
    print("Invalid Number!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    number = int(input("Enter the number: "))
    print(100/number)
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    with open("notes.txt", "r") as file:
        notes = file.read()

except FileNotFoundError:
    print("No notes file found!")