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
