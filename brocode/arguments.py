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