from car import Car

def main():
    print("This is a main function!")

if __name__ == "__main__":
    main()

    car1 = Car("BMW", "2025", "Blue", True)
    car2 = Car("Mustang", "2024", "Red", True)

    print(car1)
    print(car2)
    print(car1.color)
    print(car2.color)
