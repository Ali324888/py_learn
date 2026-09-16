numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

word = "Python"

iterator = iter(word)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

fruits = ("Apple", "Banana", "Mango")
iterator = iter(fruits)
print(next(iterator))
print(next(iterator))
print(next(iterator))

numbers = [100, 200, 300]
iterator = iter(numbers)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    