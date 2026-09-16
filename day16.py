number = 1

while number <= 10:
    print(number)
    number = number + 1

number = 10

while number > 0:
    print(number)
    number = number - 1

number = 1

while number <= 20:
    if number % 2 == 0:
        print(number)
    number = number + 1

number = int(input("Enter the number: "))

while number >= 1:
    print(number)
    number = number - 1

number = int(input("Enter the number: "))
count = 1

while count <= 10:
    print(number, " x ", count, " = ", number*count)
    count = count + 1