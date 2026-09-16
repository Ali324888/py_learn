from functools import reduce

cube = lambda number: number*number*number

print(cube(7))

numbers = [2, 4, 6, 8, 10]

twise_numbers = map(lambda number: number*2, numbers)
print(list(twise_numbers))

numbers = [10, 15, 22, 31, 40, 55, 60]
filter_numbers = filter(lambda number:number%2==0, numbers)
print(list(filter_numbers))

numbers = [10, 20, 30, 40, 50]
result = reduce(lambda a,b:a+b, numbers)
print(result)

marks = [35, 67, 82, 45, 90, 28, 76]
passing_marks = list(filter(lambda mark: mark >= 40, marks))
print(passing_marks)
bonus_marks = list(map(lambda mark:mark+5, passing_marks))
print(bonus_marks)
result = reduce(lambda a,b:a+b, bonus_marks)
print(result)
