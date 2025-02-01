# Random number

import random

a = random.random()
print(a)

a = random.randint(1,10)
print(a)

a = random.randrange(1,10)
print(a)

# if you want to pick random from a string.. use random.choices or random.sample
# shuffle a list : random.shuffle...

# reproduce your data : random.seed(n)

import secrets

a = secrets.randbelow(10)
print(a)


# DECORATORS

# Decorators are use for extending functionality of a class/function..
# adding certain functionality to a function without modifying the code of the original function..
# Wrapper class are almost same like decorators.. it just extednds the functionaility of a class...
# Types : function and class decorator

#@dosomething
def dosomething():
    pass

# let's say for a function you are expecting n number of arguments in a function then
# you can use *args, **kwargs


# Generators

# Generator is a function which can return multiple values rather than the normal function.. so it's different...
# Generator are pretty fast as we don't have to wait for the whole things to complete and you can get.. let's say the first value quickly...
# Generator object saves much more memory and are fast... 
# Another way of using the same : 

mygenerator = (i for i in range(10) if i%2==0)
print(list(mygenerator))

def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

value = next(g)
print(value)

"""
Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword is termed a generator. Hence, yield is what makes a generator.

You can use next() function for continuing the the next things after the yield keyword... 

"""

# To get the size of the variable use size function
# To get the size of a object use.. sys.getSizeof