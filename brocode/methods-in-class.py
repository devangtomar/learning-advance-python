# Instance methods = Best for operations on instances of the class (objects)

# Static methods = Best for utility functions that do not need access to class data

# Class methods = Best for class-level data or require access to the class itself

# Magic methods / Dunder methods = Dunder methods (double underscore) _init_, _str.
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects


class Employee:
    count = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):  # General utility function
        valid_position = ["Manager", "Cook"]
        return position in valid_position

    @classmethod
    def get_count(cls):
        return f"Total no of Employee: {cls.count}"

    def __str__(self):
        return f"{self.name} working as {self.position}"

print(Employee.is_valid_position("Manager"))
emp1 = Employee("spongebob", "manager")
print(Employee.get_count())
print(emp1)

