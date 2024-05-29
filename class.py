# Define a class named 'Car'
class Car:
    # Constructor method to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # Method to describe the car
    def describe_car(self):
        return f"{self.year} {self.make} {self.model}"

    # Method to read the odometer
    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    # Method to update the odometer reading
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Access attributes and call methods of the instance
print(my_car.describe_car())  # Output: 2020 Toyota Corolla
print(my_car.read_odometer())  # Output: This car has 0 miles on it.

# Update the odometer reading
my_car.update_odometer(100)
print(my_car.read_odometer())  # Output: This car has 100 miles on it.
