from staff import Staff

# Academic staff inherits from Staff
class Academic(Staff):
    def __init__(self, staff_id: int, name: str, tax_number: str, publications: int):
        super().__init__(staff_id, name, tax_number)
        self.publications = publications

    def display_details(self):
        return (
            f"Academic Staff ID: {self.staff_id}, "
            f"Name: {self.name}, "
            f"Tax Number: {self.tax_number}, "
            f"Publications: {self.publications}"
        )