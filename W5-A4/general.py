# ---------------------------------------------------------------
# general.py
# Author: Roxanne Prajapati
# Description:
#      General class inherits from Staff
# ---------------------------------------------------------------
from staff import Staff

# General staff inherits from Staff
class General(Staff):

    def __init__(self, staff_id: int, name: str, tax_number: str, pay_rate):
        # Call the constructor of the parent class Staff
        super().__init__(staff_id, name, tax_number)
        self.pay_rate = pay_rate

    def display_details(self):
        """
         Override method to display General Staff details
        """
        print (
            f"General Staff ID: {self.staff_id}, "
            f"Name: {self._name}, "
            f"Tax Number: {self.tax_number}, "
            f"Pay Rate: {self.pay_rate}"
        )