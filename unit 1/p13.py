from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]


squares = list(map(lambda x: x * x, numbers))
print("Squares using map():", squares)


evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", evens)


total = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce():", total)
