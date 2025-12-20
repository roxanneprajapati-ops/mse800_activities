# ---------------------------------------------------------------
# animal.py
# Author: Your Name
# Description:
#      This file contains all class definitions.
# ---------------------------------------------------------------


# Base Class
class Animal:
    def __init__(self, name: str):
        self.name = name


# ---------- Classes that inherits from Animal ----------
class Mammal(Animal):
    def __init__(self, name: str, feature: str):
        super().__init__(name)
        self.feature = feature


class Bird(Animal):
    def __init__(self, name: str, feature: str):
        super().__init__(name)
        self.feature = feature

class Fish(Animal):
    def __init__(self, name: str, feature: str):
        super().__init__(name)
        self.feature = feature


# ---------- Classes that inherits from Mammal ----------
class Dog(Mammal):
    def __init__(self, name: str):
        super().__init__(name, "has fur")

    def walk(self):
        print(f"{self.name} is walking.")


class Cat(Mammal):
    def __init__(self, name: str):
        super().__init__(name, "has fur")

    def walk(self):
        print(f"{self.name} is walking gracefully.")


# ---------- Classes that inherits from Bird ----------
class Eagle(Bird):
    def __init__(self, name: str):
        super().__init__(name, "Has feathers")

    def fly(self):
        print(f"{self.name} is flying.")


class Penguin(Bird):
    def __init__(self, name: str):
        super().__init__(name, "Has feathers")

    def swim(self):
        print(f"{self.name} is swimming.")


# ---------- Classes that inherits from Fish ----------
class Salmon(Fish):
    def __init__(self, name: str):
        super().__init__(name, "Has fins")

    def swim(self):
        print(f"{self.name} is swimming upstream.")


class Shark(Fish):
    def __init__(self, name: str):
        super().__init__(name, "Has fins")

    def swim(self):
        print(f"{self.name} is swimming fast.")
