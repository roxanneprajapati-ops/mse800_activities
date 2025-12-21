from person import Person

class Student(Person):
    
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.student_id = student_id
    
    def display_details(self):
        return f"Student ID: {self.student_id}, Name: {self._name}"