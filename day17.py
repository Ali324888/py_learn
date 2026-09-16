for number in range(1,11):
    if number == 5:
        break
    print(number)

for number in range(1,11):
    if number == 5:
        continue
    print(number)

for number in range(1,21):
    if number%2 == 0:
        continue
    print(number)

number = 1

while number >= 1:
    print(number)
    if number == 7:
        break
    number = number + 1

while True:
    number = int(input("Enter the number: "))
    if number == 0:
        print("Goodbye!")
        break
    print("Your number is: ", number)