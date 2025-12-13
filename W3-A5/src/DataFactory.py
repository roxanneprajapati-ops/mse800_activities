# ---------------------------------------------------------------
# DataFactory.py
# Author: Roxanne Prajapati
# Description:
#      DataFactory class holds sample data for the clinic database and provides
#      methods to insert the data into tables with error handling.
# ---------------------------------------------------------------
from datetime import date
import sqlite3

class DataFactory:

    #Patients data array
    patients = [
        (1, 'John', 'Smith', '1950-05-10', 'M', '123-4567', 'Auckland'),
        (2, 'Anna', 'Lee', '1985-03-12', 'F', '234-5678', 'Wellington'),
        (3, 'George', 'Brown', '1948-09-22', 'M', '345-6789', 'Christchurch'),
        (4, 'Mary', 'Johnson', '1955-07-30', 'F', '456-7890', 'Hamilton'),
        (5, 'Paul', 'Davis', '1970-11-15', 'M', '567-8901', 'Dunedin')
    ]

    #Doctors data array
    doctors = [
        (1, 'Emily', 'Brown', 'Ophthalmology', '999-1111'),
        (2, 'Mark', 'White', 'Cardiology', '888-2222'),
        (3, 'Laura', 'Green', 'Ophthalmology', '777-3333'),
        (4, 'James', 'Taylor', 'Dermatology', '666-4444'),
        (5, 'Sophie', 'Wilson', 'Neurology', '555-5555')
    ]

    #appointments data array
    appointments = [
        (1, '2025-12-10', 'General Checkup', 1, 1),
        (2, '2025-12-11', 'Cardiology Consultation', 2, 2),
        (3, '2025-12-12', 'Eye Exam', 3, 1),
        (4, '2025-12-13', 'Skin Rash', 4, 4),
        (5, '2025-12-14', 'Neurology Follow-up', 5, 5)
    ]

    @staticmethod
    def insert_patients(db):
        """
        Inserts patients data into the Patient table.
        Uses INSERT OR IGNORE to prevent duplicate primary key errors.
        """
        for patient in DataFactory.patients:
            try:
                db.execute(
                    "INSERT OR IGNORE INTO Patient (PatientID, FirstName, LastName, DateOfBirth, Gender, Phone, Address) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    patient
                )
            except sqlite3.IntegrityError as e:
                raise ValueError(f"Skipping duplicate patient {patient[1]} {patient[2]}: {e}")

    @staticmethod
    def insert_doctors(db):
        """
        Inserts doctors into the Doctor table.
        Uses INSERT OR IGNORE to prevent duplicate primary key errors.
        """
        for doctor in DataFactory.doctors:
            try:
                db.execute(
                    "INSERT OR IGNORE INTO Doctor (DoctorID, FirstName, LastName, Specialisation, Phone) VALUES (?, ?, ?, ?, ?)",
                    doctor
                )
            except sqlite3.IntegrityError as error:
                raise ValueError(f"Skipping duplicate doctor {doctor[1]} {doctor[2]}: {error}")


    @staticmethod
    def insert_appointments(db):
        """
        Inserts appointments into the Appointment table.
        Uses INSERT OR IGNORE to prevent duplicate primary key errors.
        """
        for appointment in DataFactory.appointments:
            try:
                db.execute(
                    "INSERT OR IGNORE INTO Appointment (AppointmentID, AppointmentDate, Reason, PatientID, DoctorID) VALUES (?, ?, ?, ?, ?)",
                    appointment
                )
            except sqlite3.IntegrityError as error:
                raise ValueError(f"Skipping duplicate appointment {appointment[0]}: {error}")

    @staticmethod
    def insert_all_data(db):
        """
        Inserts all patients, doctors, and appointments into the database.
        Safe to run multiple times without causing insertion errors.
        """
        try:
            DataFactory.insert_patients(db)
            DataFactory.insert_doctors(db)
            DataFactory.insert_appointments(db)
        except ValueError as error:
            raise ValueError(f"Error while inserting data: {error}")
