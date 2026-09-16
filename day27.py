numbers = [number for number in range(1,11)]
print(numbers)

squares = [number*number for number in range(1,11)]
print(squares)

numbers = [10, 15, 22, 31, 40, 55, 60]
even = [number for number in numbers if number%2==0]
print(even)

names = ["zee", "aman", "rahul", "priya"]
upper_names = [name.upper() for name in names]
print(upper_names)

numbers = [-10, 20, -5, 30, -2, 40]
positive_number = [number for number in numbers if number > 0]
print(positive_number)

square_dictionary = {number:number*number for number in range(1,11)}
print(square_dictionary)