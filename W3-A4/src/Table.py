# ---------------------------------------------------------------
# Table Creation
# Author: Roxanne Prajapati
# Description:
#      Contains all the table creation
# ---------------------------------------------------------------

class CampusTable:
    @staticmethod
    def create_table(db):
        db.execute("""
            CREATE TABLE IF NOT EXISTS Campus(
                CampusID INTEGER PRIMARY KEY,
                CampusName TEXT,
                Location TEXT,
                PhoneNumber TEXT
            )
        """)


class InstructorTable:
    @staticmethod
    def create_table(db):
        db.execute("""
            CREATE TABLE IF NOT EXISTS Instructor(
                InstructorID INTEGER PRIMARY KEY,
                CampusID INTEGER,
                FirstName TEXT,
                LastName TEXT,
                Email TEXT,
                FOREIGN KEY (CampusID) REFERENCES Campus(CampusID)
            )
        """)


class StudentTable:
    @staticmethod
    def create_table(db):
        db.execute("""
            CREATE TABLE IF NOT EXISTS Student(
                StudentID INTEGER PRIMARY KEY,
                CampusID INTEGER,
                FirstName TEXT,
                LastName TEXT,
                DateOfBirth TEXT,
                Email TEXT,
                Major TEXT,
                FOREIGN KEY (CampusID) REFERENCES Campus(CampusID)
            )
        """)


class CoursesTable:
    @staticmethod
    def create_table(db):
        db.execute("""
            CREATE TABLE IF NOT EXISTS Courses(
                CourseID TEXT PRIMARY KEY,
                InstructorID INTEGER,
                CourseName TEXT,
                Credits INTEGER,
                RoomNumber TEXT,
                FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
            )
        """)


class EnrolsTable:
    @staticmethod
    def create_table(db):
        db.execute("""
            CREATE TABLE IF NOT EXISTS Enrols(
                StudentID INTEGER,
                CourseID TEXT,
                FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
                FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
            )
        """)