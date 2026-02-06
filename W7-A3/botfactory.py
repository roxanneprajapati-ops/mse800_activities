from abc import ABC, abstractmethod

class Unit(ABC):
    # Unit Class is the abstract base class that defines a common interface 
    # for all unit types
    def __init__(self, id):
        self.id = id

    @abstractmethod
    # This abstract method forces the subclasses to provide their own behaviour
    def action(self):
        pass

class Helper(Unit):
    # Concrete implementation of Unit
    def action(self):
        print(f"{self.id} is assisting humans")

class Friend(Unit):
    # Another concrete implementation of Unit
    def action(self):
        print(f"{self.id} is keeping company")

class Maker:
    @staticmethod
    def produce(unit_type, id):
        # Factory pattern: Encapsulates object creation logic
        if unit_type == "helper":
            return Helper(id)
        elif unit_type == "friend":
            return Friend(id)
        else:
            raise ValueError("Unknown type")
