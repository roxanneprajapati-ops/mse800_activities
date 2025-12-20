from person import Person

class Staff(Person):
    
    def __init__(self, staff_id, name, tax_number):
        super().__init__(staff_id, name)
        self.staff_id = staff_id
        self.tax_number = tax_number

    def display_info(self):
        return (
            f"Staff ID: {self.staff_id}, "
            f"Name: {self.name}, "
            f"Tax Number: {self.tax_number}"
        )