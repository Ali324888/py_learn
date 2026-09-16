age = int(input("Enter age: "))
has_id = True

if has_id and age >= 18:
    print("Entry allowed")
else:
    print("Entry Denied")

day = input("Enter day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

is_raining = False

if not is_raining:
    print("Go outside")
else: 
    print("Do not go out")
number = int(input("Enter the number: "))

if number >= 10 and number <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is outside")

username = input("Username: ")
password = input("Password: ")

if username == "zee" and password == "123":
    print("Login Successful")
else:
    print("Invalid Credential!")

total = int(input("Enter total: "))
is_member = input("Are you a member? (yes/no): ")

if total >= 1000 and is_member == "yes":
    print("10% discount")
else:
    print("No discount")

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age >13 and age < 20:
    print("Teenager")
elif age>19 and age<60:
    print("Adult")
else:
    print("Senior")