# ---------------------------------------------------------------
# main.py
# Author: Roxanne Prajapati
# Description:
#      This program demonstrates inheritance by creating Student, General,
#      and Academic objects and displaying their details.
# ---------------------------------------------------------------

# Import classes
from student import Student
from general import General
from academic import Academic

def main():
    """
    Main function to run the program.
    """
    # Create student, general staff, academic staff objects
    student = Student(101, "Alice")
    general_staff = General(201, "Bob", "TX12345", 30.5)
    academic_staff = Academic(301, "Dr. Smith", "TX67890", 12)

    # Display details of each object
    print(student.display_details())
    print(general_staff.display_details())
    print(academic_staff.display_details())


# Run the program only when executed directly
if __name__ == "__main__":
    main()
