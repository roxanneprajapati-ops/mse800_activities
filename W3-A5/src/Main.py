# ---------------------------------------------------------------
# Main.py
# Author: Roxanne Prajapati
# Description:
#      Entry point of the clinic OOP project responsible for
#      setting up the database by initializing the connection,
#      creating tables, inserting sample data,
#      executing specific queries
#      (senior patients and ophthalmology doctor count),
#      and handling any execution errors.
# ---------------------------------------------------------------
from DatabaseManager import DatabaseManager
from DataFactory import DataFactory
from Tables import Tables

def main():
    # Initialize database
    database_manager = DatabaseManager()
    try:
        #Create tables
        Tables.create_all_tables(database_manager)

        #Insert clinic data
        DataFactory.insert_all_data(database_manager)

        #Retrieve the list of all senior patients with age above 65
        seniors = database_manager.fetch_all("""
            SELECT * FROM Patient
            WHERE (strftime('%Y','now') - strftime('%Y', DateOfBirth)) > 65
        """)

        print("Senior Patients:")
        for seniors in seniors:
            print(seniors)

        #Retrieve the count of ophthalmology doctors
        optalmologists = database_manager.fetch_all("""
            SELECT COUNT(*) FROM Doctor
            WHERE Specialisation = 'Ophthalmology'

        """)

        print("Total Ophthalmology Doctors:", optalmologists[0][0])

    except ValueError as error:
        print(f"An error occurred during execution: {error}")
    finally:
        database_manager.close()


if __name__ == "__main__":
    main()
