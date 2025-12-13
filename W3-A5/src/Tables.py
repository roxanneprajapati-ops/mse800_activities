# ---------------------------------------------------------------
# Tables.py
# Author: Your Name
# Description:
#      Tables class contains all database table definitions
#      Each method creates a table and includes error handling
# ---------------------------------------------------------------

class Tables:

    @staticmethod
    def create_patient_table(db):
        # Create Patient table to store patient demographic information
        try:
            db.execute("""
            CREATE TABLE IF NOT EXISTS Patient (
                PatientID INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                DateOfBirth DATE,
                Gender TEXT,
                Phone TEXT,
                Address TEXT
            )
            """)
        except Exception as error:
            raise ValueError(f"Error creating Patient table: {error}")

    @staticmethod
    def create_doctor_table(db):
        # Create Doctor table to store doctor details and specialisation
        try:
            db.execute("""
            CREATE TABLE IF NOT EXISTS Doctor (
                DoctorID INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                Specialisation TEXT,
                Phone TEXT
            )
            """)
        except Exception as error:
            raise ValueError(f"Error creating Doctor table: {error}")

    @staticmethod
    def create_appointment_table(db):
        # Create Appointment table linking patients and doctors
        try:
            db.execute("""
            CREATE TABLE IF NOT EXISTS Appointment (
                AppointmentID INTEGER PRIMARY KEY,
                AppointmentDate DATE,
                Reason TEXT,
                PatientID INTEGER,
                DoctorID INTEGER,
                FOREIGN KEY(PatientID) REFERENCES Patient(PatientID),
                FOREIGN KEY(DoctorID) REFERENCES Doctor(DoctorID)
            )
            """)
        except Exception as error:
            raise ValueError(f"Error creating Appointment table: {error}")

    @staticmethod
    def create_all_tables(db):
        # Create all tables in correct order
        try:
            Tables.create_patient_table(db)
            Tables.create_doctor_table(db)
            Tables.create_appointment_table(db)
        except Exception as error:
            raise ValueError(f"Error creating tables: {error}")

