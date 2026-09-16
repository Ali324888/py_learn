number = (10,20,30,40,50)

print(number)
print(number[0])
print(number[2])
print(number[-1])
print(len(number))

cities = ("Jaipur", "Delhi", "Mumbai")
cities[1] = "Kota" #gives error due immutability

numbers = {10, 20, 10, 30, 20, 40, 10}
print(numbers)

fruits = {"Apple", "Banana"}
fruits.add("Mango")
fruits.remove("Banana")
print(fruits)

names = ["Zee", "Aman", "Zee", "Rahul", "Aman", "Priya"]
unique_name = set(names)
print(unique_name)