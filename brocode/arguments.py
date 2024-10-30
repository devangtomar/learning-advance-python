def net_price(price, tax=0.07):
    return price + price * tax


print(net_price(100))  # 107.0
print(net_price(100, 0.1))  # 110.0


def net_price(price, tax=0.07):
    return price + price * tax


print(net_price(100, tax=0.1))  # 110.0
print(net_price(100, 0.1))  # 110.0


# Keyword-only arguments
def net_price(price, *, tax=0.07):
    return price + price * tax


print(net_price(100))  # 107.0


def hello(greeting, name):
    print(f"{greeting}, {name}!")


hello("Hello", "Alice")  # Hello, Alice!
hello("Hello", name="Alice")  # Hello, Alice!
hello(greeting="Hello", name="Alice")  # Hello, Alice!

# arbitrary number of arguments


def my_function(*args):
    print(type(args))
    print(args, sep="-")
    for arg in args:
        print(arg)


my_function(1, 2, 3, 4, 5)

# **kwargs


def my_function(**kwargs):
    print(type(kwargs))
    print(kwargs, sep="-")
    for key, value in kwargs.items():
        print(key, value, sep="-")


my_function(a=1, b=2, c=3)

# combining number of arguments of positional, keyword, *args, and **kwargs


def my_function(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args, sep="-")
    print(kwargs, sep="-")
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value, sep="-")


my_function(1, 2, 3, 4, 5, a=1, b=2, c=3)
