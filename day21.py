import random

secret_number = random.randint(1,20)
# print(secret_number)

attempt = 0

while True:
    input_number = int(input("Enter the guess number: "))

    attempt = attempt + 1

    if attempt == 10:
        print("Game over!")
        break

    if input_number == secret_number:
        print("You guess correct! 🎉")
        print("Your Attempt: ",attempt)
        break
    elif input_number > secret_number:
        print("Too high")
    else:
        print("Too low")