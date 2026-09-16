# firstNumber = int(input("First Number: "))
# secondNumber = int(input("Second Number: "))
# operator = input("Enter Operation (+,-,*,/,%): ")

# if operator == "+":
#     print("Result: ", firstNumber+secondNumber)
# elif operator == "-":
#     print("Result: ", firstNumber-secondNumber)
# elif operator == "*":
#     print("Result: ", firstNumber*secondNumber)
# elif operator == "/":
#     if secondNumber == 0:
#         print("Number cannot be devided by zero")
#     else:
#         print("Result: ", firstNumber/secondNumber)
# elif operator == "%":
#     print("Result: ", firstNumber%secondNumber)
# elif operator == "//":
#     if secondNumber == 0:
#         print("Number cannot be devided by zero")
#     else:
#         print("Result: ", firstNumber//secondNumber)
# elif operator == "**":
#     print("Result: ", firstNumber**secondNumber)
# else:
#     print("Invalid operation")

price = int(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))

total = price*quantity

if total >= 1000 :
    discount = total*0.1
else:
    discount = 0


print("Total: ", total)
print("Discount: ", discount)
print("Final Price: ", total - discount)