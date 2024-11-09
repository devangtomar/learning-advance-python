class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(
            f"You drive the {self.model} with color {self.color} which is on sale or not: {self.for_sale}!"
        )

    def stop(self):
        print(
            f"You stopped the {self.model} with color {self.color} which is on sale or not: {self.for_sale}!"
        )
