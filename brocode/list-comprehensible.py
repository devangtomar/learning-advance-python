doubles = [x * 2 for x in range(0, 10)]
print(doubles)

squares = [x**2 for x in range(0, 10)]  # or [x * x for x in range(0, 10)]
print(squares)

fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)

fruits = ["apple", "banana", "cherry"]
lengths = [len(fruit) for fruit in fruits]
print(lengths)

fruits = ["apple", "banana", "cherry"]
filtered_fruits = [fruit for fruit in fruits if "a" in fruit]
print(filtered_fruits)

numbers = [1, 2, 3, 4, -1, -2, -3]
positive_nums = [num for num in numbers if num > 0]
even_nums = [num for num in numbers if num % 2 == 0]
print(f"Positive numbers: {positive_nums}")
print(f"Even numbers: {even_nums}")
