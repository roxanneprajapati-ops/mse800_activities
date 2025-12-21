# ---------------------------------------------------------------
# staff.py
# Author: Roxanne Prajapati
# Description:
#      Students class inherits from Person
# ---------------------------------------------------------------

from person import Person

class Staff(Person):

    def __init__(self, staff_id, name, tax_number):
        # Call the constructor of the parent class
        super().__init__(staff_id, name)
        self.staff_id = staff_id
        self.tax_number = tax_number

    def display_info(self):
        """
         Override method to display student details
        """
        return (
            f"Staff ID: {self.staff_id}, "
            f"Name: {self._name}, "
            f"Tax Number: {self.tax_number}"
        )