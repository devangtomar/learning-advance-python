# Lists : ordered, mutable, allows duplicate values..

mylist = [1,2,3,4,5]
another_list = [0] * 5
print(another_list)

print(mylist)
print(mylist[:-1]) # slicing..
print(mylist[::2]) # 2 steps skip
print(mylist[::-1]) # reverse the list without using reverse function..

# to copy a list either use a copy() or use a list function  or use slicing for the same..
another_list = mylist.copy()
print(another_list)


new_list =  [i*i for i in mylist]
print(new_list)

# Tuples : ordered , in-mutable, allows duplicate values

mytuple = ("Max", 26, "Boston")  # Paranthesis are optional..
print(mytuple)

# A tuple can have a single element but you need to use , towards the end...

mytuple = ("Max")
print(type(mytuple))

mytuple = ("Max",)
print(type(mytuple))

# You can also use a tuple functions..

mytuple = tuple(["max", 26, "Boston", "p"])
print(mytuple)
print(mytuple[-1])

# Tuple doesn't allow assignment...

for x in mytuple:
    print(x)

if "Boston" in mytuple:
    print("It's there!")

print(len(mytuple))
print(mytuple.count('l'))
print(mytuple.index('p'))

# Same slicing like lists...
print(mytuple[::-1])

name, age, city, character = mytuple
print(name)
print(age)
print(city)
print(character)

# Compare a list and a tuple..
# tuples are fast ..

# Dictionary : {} 
# key : values

mydict = {"name" : "max", "age" :  28, "city" : "Boston"}

print(mydict)
print(mydict["name"])

mydict["name"] = "Devang"
print(mydict["name"])

# Delete..

del mydict["name"]
print(mydict)

mydict.popitem()
print(mydict)


mydict = {"name" : "max", "age" :  28, "city" : "Boston"}

try:
    print(mydict["name"])
except:
    print(mydict["name"])

for key in mydict.values():  # items..
    print(key)
    
# you can use dict() and copy() fucntion for copying the dictionary...
# for merging dictionary.. :
mydict.update(mydict)

# List is not hashable and cannot be used in dictionary while tuple can be...

#SET : unordered, mutable and no duplications are allowerd..

myset = set("Hello")
print(myset) # for counting what all the elements are there..

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

for i in myset:
    print(x)

# common operations on sets : .union(), .intersection(), .difference(), synnetric_difference(), 
# somoe more operations : .update(), .intersection_update(), difference_update(), 
# some more operations : .symmetric_difference_update()

# Subset, superset and join method..
# .issubset(), .issuperset(), isdisjoint()

# Copying two sets...
# .copy()

# Forzen set.. 

a = frozenset([1,2,3,4])

#a.add(3) # will give an error
# union etc. will work...



# STRING 
# ordered, immutable, text representation

string = "I'm a programmer"
another_string = ''
new_string = """

this
is
a
multiline
string

"""

print(string[1:5])

# concatenate...

greetings = "hello"
print(greetings+string)

for i in greetings:
    print(i)

if "e" in greetings:
    print("yes")

string = "    Hello World"
print(string.strip())
print(string.startswith("H"))
print(string.endswith("a"))
print(string.find("a"))
print(string.count('a'))
print(string.replace('world', 'New world'))

# to convert into list

my_list = string.split(" ")
print(my_list)

# to convert back....
# don't interate through loop because it's really extensive on the CPU

new_string = ' '.join(my_list)
print(new_string)

my_list = ['a'] * 6
print(my_list)

# for measuring the time b/w...

from functools import reduce
from timeit import default_timer as timer

start = timer()
stop = timer()
print(stop-start)

# %, format(), f-strings

var = 3
my_string = "The variable is %s" % var
my_string = "The variable is %d" % var # for integer
my_string = "The variable is %f" % var # for float values
my_string = "The variable is %.2f" % var # for float values and 2 digit after decimal points..

# New method : format()

my_string = "The variable is {}".format(var)
my_string = "The variable is %.2f".format(var)

# in f-strings : New in python 3.6

my_string = f"The variable is {var*2}"

print(my_string)

# Collections : Counter, namedtuple, OrderedDict, Defaultdict, deque

from collections import Counter

a = "aaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))



from collections import namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1, -4)
print(pt)
print(pt.x)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
print(ordered_dict)

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])

from collections import deque
# double ended Qs
d = deque()

d.appendleft(3)
print(d)

d.pop()
print(d)

d.clear()
print(d)

d.extendleft([3,5,6])
print(d)

d.rotate(2)
print(d)

d.rotate(-1)
print(d)

# Itertools : product, permutations,combinations , accumulate, groupby and infinite iterators

from itertools import permutations, product, combinations
from itertools import combinations_with_replacement
from itertools import accumulate
from itertools import groupby


a = [1,2]
b = [3,4]
print(list(product(a,b, repeat=2)))

a = [1,2,3]
print(list(permutations(a)))
print(list(permutations(a, 2)))

a = [1,2,3]
print(list(combinations(a, 2)))

print(list(combinations_with_replacement(a, 2)))

acc = accumulate(a, func=max)
print(list(accumulate(a)))
print(list(acc))

def smaller_than_3(x):
    return x < 3

group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))


from itertools import count, cycle, repeat

# count will make a infinite loop
# cycle will repeat a certain range
# repeat will keep print.. repeat(1, 4) - print 1 four times...

# Lambda functions...

# lambda arguments: expression

add10 = lambda x: x+10
print(add10(5))

points2D = [(1,2),(3,4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)
print(points2D)

points2D_sorted = sorted(points2D, key=lambda x: x[1] + x[0])
print(points2D_sorted)

# map(func, seq)

a =[1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

# can also be implemented as :
b = [x*2 for x in a]
print(b)

# filter(func, seq)
b = filter(lambda x:x%2==0, a)
print(list(b))

# can also be implemented as :
b = [x for x in a if x%2==0]
print(b)

# Reduce functions...

a =[1,2,3,4,5]
product_a = reduce(lambda x,y:x*y, a)
print(product_a)

# EXCEPTIONS and ERRORs
# Type or error : syntax and exceptiom
# types of error : type-error, import-error, name error, file not found error
# more error : value-error, index-error

# x = -4
# if x < 0:
#     raise Exception('x should be positive')


# assert(x>=0), 'x is not positive'

# try:
#     a = 5 / 0
# except:
#     print("An error happened..")


# try:
#     a = 5 / 0
# except Exception as e:
#     print(f"An error happened.. {e}")



try:
    a = 5 / 0
except ZeroDivisionError as e:
    print(f"An error happened.. {e}")
except TypeError as e:
    print(e)
else:
    # if no exception occurs..
    print("everthing is okay")
finally:
    # will be always executed..
    print('cleaning up...')


# make your own exception...

# class ValueTooHighError(Exception):
#     pass

# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('Value is too high')
    
# try:
#     test_value(200)
# except:
#     print(e)

#JSON

# to convert a dictionary into a JSON.. use dumps() and 
# for transfering a json into a file use dump()

# to change json > dictionary.. use loads() and for file use load()

# 'self' keyword is there for accessing class fucnctions and variables
# '___init___' is a constructor of the class
# 'del' is use for destructor.. ideally it's called.. but you can call it explicitly..


# for encoding a object in a json : JSON encoder...
# for de-coding.. use 