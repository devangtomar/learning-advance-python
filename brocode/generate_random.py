from random import randint
import random

number = randint(1, 10)
print(number)

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=2))
print(random.sample([1, 2, 3, 4, 5], k=2))
print(random.shuffle([1, 2, 3, 4, 5]))
print(random.seed(42))