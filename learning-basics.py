from functools import reduce


def add(x, y):
    return x + y


def even(x):
    return x % 2 == 0


def multiple(x):
    return x * 5


fruits = [1, 2, 3, 4, 5]

lambda_add_5 = lambda x: [i + 5 for i in x]

reduce_add = reduce(add, fruits)
filter_even = filter(even, fruits)
map_multiply_by_5 = map(multiple, fruits)

print(fruits)
print(reduce_add)
print(list(filter(even, fruits)))
print(list(map_multiply_by_5))

# easy loop

print([i for i in fruits])
print([i for i in fruits if i % 2 == 0])

# Decorator..


def decorator(func):
    def wrapper():
        print("This is the start!")
        func()
        print("This is the end!")

    return wrapper


@decorator
def print_something():
    print("This is a function!")


print_something()

# Generator..


# Define a generator function that yields the square of each number in the input list
def square_generator(numbers):
    for num in numbers:
        yield num**2


# Input list of numbers
numbers = [1, 2, 3, 4, 5]

# Using the square_generator to generate squares of numbers
squared_nums = square_generator(numbers)
example = lambda x : x ** 2
print([x for x in squared_nums])
print(example(4))

# some list stuff..

print(fruits[:-1])
print(fruits[::-2])