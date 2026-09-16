fruits = ["Apple", "Banana", "Mango"]
# fruits.append('Orange')
fruits.insert(1, 'Orange')
print(fruits)

cities = ["Jaipur", "Delhi", "Mumbai", "Kota"]
cities.remove("Delhi")
print(cities)

# numbers = [50, 10, 40, 20, 30]
# numbers.sort()
# numbers.pop()
# print(numbers)

numbers = [10, 20, 10, 30, 10, 40]
print(numbers.count(10))
print(numbers.index(30))
numbers.reverse()
print(numbers)