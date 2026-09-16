def numbers():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

generator = numbers()

for number in generator:
    print(number)

def square_numbers(start, end):
    for number in range(start, end+1):
        yield number*number

gen = square_numbers(1,5)

for num in gen:
    print(num)

def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"

fal = fruits()

print(next(fal))
print(next(fal))
print(next(fal))


def even_numbers(start, end):
    for number in range(start, end+1):
        if number%2 == 0:
            yield number

sam_sankhya = even_numbers(1,20)

for number in sam_sankhya:
    print(number)