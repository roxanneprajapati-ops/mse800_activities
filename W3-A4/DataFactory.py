# ---------------------------------------------------------------
# College Data Factory
# Author: Roxanne Prajapati
# Description:
#      This file holds all the data to be inserted into tables.
# ---------------------------------------------------------------

class DataFactory:

    @staticmethod
    def campuses():
        return [
            (1, "City Road Campus", "Auckland", "111-1111"),
            (2, "345 Queen Street", "Auckland", "222-2222")
        ]

    @staticmethod
    def instructors():
        return [
            (1, 1, "John", "Smith", "john@college.com"),
            (2, 1, "Emma", "Brown", "emma@college.com"),
            (3, 2, "Liam", "Davis", "liam@college.com")
        ]

    @staticmethod
    def students():
        return [
            (1, 1, "Alex", "Lee", "2001-01-01", "alex@yoobee.com", "MSE"),
            (2, 1, "Mia", "Chen", "2002-05-10", "mia@yoobee.com", "MBI"),
            (3, 2, "Noah", "Park", "2001-03-14", "noah@yoobee.com", "MSE")
        ]

    @staticmethod
    def courses():
        return [
            ("MSE800", 1, "Professional Software Engineering", 120, "Room 412"),
            ("MSE801", 2, "Research Method", 120, "Room 403"),
            ("MSE802", 3, "Quantum Computing", 120, "Room 412")
        ]

    @staticmethod
    def enrols():
        # StudentID, CourseID
        return [
            (1, "MSE800"),
            (2, "MSE800"),
            (3, "MSE800"),
            (1, "MSE801"),
            (2, "MSE801"),
            (3, "MSE801"),
            (1, "MSE802"),
            (2, "MSE802"),
            (3, "MSE802")
        ]
