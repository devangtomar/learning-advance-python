class Prey:
    def flee(self):
        print(f"The animal {self.__class__} is fleeing!")

class Predator:
    def hunt(self):
        print("The animal is hunting!")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()