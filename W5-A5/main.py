# ---------------------------------------------------------------
# main.py
# Author: Roxanne Prajapati
# Description:
#      The main.py file acts as the entry point of the program and is
#      responsible for running the application. It creates objects
#      from the animal classes defined in animals.py and demonstrates
#      their different behaviours.
#
#       Part 2:
#       Yes, different objects can respond differently to the
#       same method call through polymorphism, where related
#       classes use the same method name but perform different actions.
# ---------------------------------------------------------------

from animals import Dog, Cat, Eagle, Penguin, Salmon, Shark
def main():
    """
    Main function to run the program.
    """
    # Create objects of different animal types
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Eagle("Sky"),
        Penguin("Pingu"),
        Salmon("Nemo"),
        Shark("Mako")
    ]
    # Call the appropriate behaviour for each animal
    for animal in animals:
        if hasattr(animal, "walk"):
            animal.walk()
        elif hasattr(animal, "fly"):
            animal.fly()
        elif hasattr(animal, "swim"):
            animal.swim()


# Run the program only when executed directly
if __name__ == "__main__":
    main()