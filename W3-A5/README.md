# Clinic OOP Project

## Project Overview

This project is an OOP-based clinic management system,developed with Python and SQLite, designed to handle patient records, doctor information, and appointment scheduling.

The project supports:
* Listing all patients aged over 65 (senior patients)
* Counting the total number of doctors specialising in ophthalmology

## Project Structure
- src/
  - DatabaseManager.py  # Handles database connection, execution of SQL commands, and query results
  - DataFactory.py      # Inserts sample data into the database for testing and demonstration
  - Table.py            # Contains all table creation logic with error handling
  - Main.py             # Entry point of the application; creates tables and executes required queries
  - clinic.db           # SQLite database file storing all clinic data
- README.md             # Provides an overview of the project
- clinic_ERD.png        # Visual representation of the database ER diagram



## Notes
* Error handling is implemented for table creation and main execution.
* Comments and file descriptions are included for clarity and maintainability.

## Author
Roxanne Prajapati
