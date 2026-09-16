number = int(input("Enter the number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
elif number == 0:
    print("zero")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

marks = int(input("Enter your marks: "))

if marks >=90:
    print("A+")
elif marks >=80:
    print("A")
elif marks >=70:
    print("B")
elif marks >=60:
    print("C")
elif marks >=50:
    print("D")
else:
    print("Fail")

number = int(input("Enter the number: "))

if number > 0:
    if number%2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif number < 0:
    if number%2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
elif number == 0:
    print("Zero")

username = input("Username: ")
password = input("Password: ")

if username == "zee" and password == "123":
    print("Login Successful")
else:
    print("Invalid Credential!")

balance = 10000
withdrawal = int(input("Withdrawal: "))

if withdrawal <= balance:
    print("Withdrawal successful")
elif withdrawal <= 0:
    print("Invalid amount")
else:
    print("Insuficiant balance")