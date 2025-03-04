# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
# Benefit: Add additional logic when read, write, or delete attributes
# Gives you getter, setter, and deleter method


class Rectangle:
    def __init__(self, height, width):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width: .1f}cm"

    @property
    def height(self):
        return f"{self._height: .1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be more than 0!")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted!")


rectangle = Rectangle(3, 4)
rectangle.width = 0
print(rectangle.width)
print(rectangle.height)
print(rectangle._width)
print(rectangle._height)

del rectangle.width

# Decorator = A function that extends the behavior of another function
# w/o modifying the base function
# Pass the base function as an argument to the decorator
# @add_sprinkles get_ice_cream("vanilla")


def add_sprinkles(func):
    def wrapper():
        print("*You adding sprinkles!*")
        func()

    return wrapper


@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream")


get_ice_cream()
