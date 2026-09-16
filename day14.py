score = 0

answer = input("Python kis type ki language hai? ")

if answer == "programming":
    print("Correct")
    score = score + 1
else:
    print("incorrect")

answer = input("What is 5 + 5? ")

if answer == "10":
    print("Correct")
    score = score + 1
else:
    print("incorrect")

answer = input("Which data type stores True or False? ")

if answer == "bool":
    print("Correct")
    score = score + 1
else:
    print("incorrect")

answer = input("Which symbol is used for equality comparison? ")

if answer == "==":
    print("Correct")
    score = score + 1
else:
    print("incorrect")

answer = input("Which collection does not allow duplicate values? ")

if answer == "set":
    print("Correct")
    score = score + 1
else:
    print("incorrect")


print("Final Score:", score, "/ 5")


if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")