class KeeperMeta(type):
    _holders = {}
    def __call__(cls, *args, **kwargs):
        # Singleton pattern: Only one instance of class is created and used for all units
        if cls not in cls._holders:
            instance = super().__call__(*args, **kwargs)
            cls._holders[cls] = instance
        return cls._holders[cls]

class Keeper(metaclass=KeeperMeta):
    
    def __init__(self):
        # Stores the collection of units managed by the application
        self.units = []

    def add_unit(self, unit):
        # Adds a unit to the shared manager instance
        self.units.append(unit)
