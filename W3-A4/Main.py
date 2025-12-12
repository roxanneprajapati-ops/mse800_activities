# ---------------------------------------------------------------
# Main program
# Author: Roxanne Prajapati
# Description:
#       Contains the main programs that creates table and insert data
#       to the college DB and perform db search
# ---------------------------------------------------------------

from DatabaseManager import DatabaseManager
from DataFactory import DataFactory
from Table import CampusTable, InstructorTable, StudentTable, CoursesTable, EnrolsTable

def main():
    # Initialize the DatabaseManager to handle all DB connections
    database_manager = DatabaseManager()
    try:
        # Create all tables
        CampusTable.create_table(database_manager)
        InstructorTable.create_table(database_manager)
        StudentTable.create_table(database_manager)
        CoursesTable.create_table(database_manager)
        EnrolsTable.create_table(database_manager)

        # Insert data into tables
        for campus in DataFactory.campuses():
            database_manager.execute("INSERT INTO Campus VALUES (?,?,?,?)", campus)

        for instructor in DataFactory.instructors():
            database_manager.execute("INSERT INTO Instructor VALUES (?,?,?,?,?)", instructor)

        for student in DataFactory.students():
            database_manager.execute("INSERT INTO Student VALUES (?,?,?,?,?,?,?)", student)

        for course in DataFactory.courses():
            database_manager.execute("INSERT INTO Courses VALUES (?,?,?,?,?)", course)

        for enrol in DataFactory.enrols():
            database_manager.execute("INSERT INTO Enrols VALUES (?,?)", enrol)

        # Query: number of students in MSE800
        students = database_manager.fetch_all("""SELECT COUNT(*) FROM Enrols WHERE CourseID='MSE800'""")
        print("Students in MSE800:", students[0][0])

        # Query: list instructors teaching MSE801
        instructors = database_manager.fetch_all("""
            SELECT FirstName, LastName
            FROM Instructor 
            JOIN Courses ON Instructor.InstructorID = Courses.InstructorID
            WHERE CourseID='MSE801'
        """)

        print("Instructors teaching MSE801:")
        for instructor in instructors:
            print(instructor[0], instructor[1])

        database_manager.close()
    except ValueError as error:
        print(error)
    finally:
        database_manager.close()

if __name__ == "__main__":
    main()
