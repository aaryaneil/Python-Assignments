# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

# Multiple Inheritance
class Flyer:
    def fly(self):
        return "Fly"

class Swimmer:
    def swim(self):
        return "Swim!"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

# Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return "Drive"

class Car(Vehicle):
    def honk(self):
        return "Beep!"

class ElectricCar(Car):
    def charge(self):
        return "Charge"


    # Single Inheritance Example
dog = Dog("Marley")
print(f"{dog.name} says: {dog.speak()}")

    # Multiple Inheritance Example
duck = Duck()
print(f"Duck: {duck.fly()}")
print(f"Duck: {duck.swim()}")
print(f"Duck: {duck.quack()}")

    # Multilevel Inheritance Example
tesla = ElectricCar("Tesla")
print(f"{tesla.brand} is {tesla.drive()}")
print(f"{tesla.brand} goes {tesla.honk()}")
print(f"{tesla.brand} is {tesla.charge()}")