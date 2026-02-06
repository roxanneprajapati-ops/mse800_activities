from core import Keeper
from botfactory import Maker
from tracker import Screen, Record

# Singleton pattern: Keeper() always returns the same instance to have 
# one shared manager for all units
manager = Keeper()

# Observer pattern: Screen and Record are observers for 
screen = Screen()
record = Record()

# Factory pattern: Objects are created through Maker instead of 
# instantiating classes directly
unit1 = Maker.produce("helper", "AlphaBot")
unit2 = Maker.produce("friend", "BetaBot")

# Singleton manager keeps track of all created units
manager.add_unit(unit1)
manager.add_unit(unit2)

for unit in manager.units:
    # Each unit responds to action() differently depending on unit type
    unit.action()

    # Screen and record are notified when a unit completes an action
    # This does not change unit logic
    screen.notice(f"{unit.id} completed an action")
    record.notice(f"{unit.id} completed an action")
