# ---------------------------------------------------------------
# Encapsulation Activity
# Author: Roxanne Prajapati
# Explanation:
#      The self._name in Person and Staff will display the same value
#      since Staff inherits from Person, because self._name is a
#      protected attribute stored in the same object instance.
#
#      Protected attributes from a base class are accessible to child classes,
#      so Staff can directly use self._name without redefining it.
# ---------------------------------------------------------------

class Person:

    def __init__(self, name, address, age):
        self._name = name
        self.address = address
        self.age = age


    def greet(self):
        print("Greetings and felicitations from the maestro " + self._name)


class Student(Person):

    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age)
        self.student_id = student_id

    def greet(self):
        print("Hi " + self._name)


def main():
    """Demonstration of encapsulation"""
    student = Student("Alice", "123 Main St", 22, "S1234")
    student.greet()

# Run the program only when executed directly
if __name__ == "__main__":
    main()
