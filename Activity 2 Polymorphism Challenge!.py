class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} makes a generic movement.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs on four legs.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies through the air.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims in the water.")

class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"{self.model} makes a generic movement.")

class Car(Vehicle):
    def move(self):
        print(f"{self.model} is driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.model} is flying in the sky. ✈️")

# Creating instances of different classes
animal1 = Dog("Buddy")
animal2 = Bird("Tweety")
animal3 = Fish("Nemo")
vehicle1 = Car("Sedan")
vehicle2 = Plane("Boeing 747")

# Creating a list of objects
things_that_move = [animal1, animal2, animal3, vehicle1, vehicle2]

# Demonstrating polymorphism
print("--- Polymorphism in Action ---")
for thing in things_that_move:
    thing.move()