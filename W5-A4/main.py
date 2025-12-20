# ---------------------------------------------------------------
# TITLE HERE
# Author: Your Name
# Description:
#      
# ---------------------------------------------------------------
from student import Student
from general import General
from academic import Academic

def main():
    """
    Main function to run the program.
    """
    student = Student(101, "Alice")
    general_staff = General(201, "Bob", "TX12345", 30.5)
    academic_staff = Academic(301, "Dr. Smith", "TX67890", 12)

    print(student.display_details())
    print(general_staff.display_details())
    print(academic_staff.display_details())


# Run the program only when executed directly
if __name__ == "__main__":
    main()
