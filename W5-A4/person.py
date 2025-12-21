class Person:
    
    def __init__(self, person_id, name):
        self.person_id = person_id
        self._name = name
    
    def display_details(self):
        return f"ID: {self.person_id}, Name: {self._name}"