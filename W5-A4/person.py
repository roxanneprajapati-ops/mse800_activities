# ---------------------------------------------------------------
# person.py
# Author: Roxanne Prajapati
# Description:
#      This file defines the Person class, which acts as a base class in the
#      project. It stores common attributes such as person ID and name, and provides
#      a method to display basic person details.
# ---------------------------------------------------------------
class Person:
    
    def __init__(self, person_id, name):
        self.person_id = person_id
        self._name = name
    
    def display_details(self):
        return f"ID: {self.person_id}, Name: {self._name}"