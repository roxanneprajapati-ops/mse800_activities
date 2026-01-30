# Currency Exchange CLI Application

## Overview
This project is a **small-scope command-line (CLI) currency exchange application** developed in Python.  
It allows users to **view the current exchange rate**, **update the exchange rate**, and **convert an amount** between one base currency and one target currency.

The application is intentionally simple and focuses on demonstrating **core Object-Oriented Programming (OOP) concepts**, **backend architecture**, **database design**, **error handling**, and **logging**, as required for Week 6 Activity 8.

---

## Features
- View the current exchange rate
- Update the exchange rate manually
- Convert an amount using the stored rate
- Persist data using a local SQLite database
- Validate user input and handle errors safely
- Log important actions and errors for debugging

---

## OOP Concepts Applied

### Encapsulation
- Domain models (`ExchangeRate`, `Conversion`) use **protected attributes** (e.g. `_rate`, `_amount`)
- Access and modification are controlled through **properties and setters**
- Validation logic is enforced within the models to maintain object integrity

### Abstraction
- The CLI layer interacts only with high-level service methods
- Database logic is hidden behind the `DatabaseManager` class
- Business rules are isolated in the `ExchangeService` layer

### Design Pattern: Singleton
- `DatabaseManager` is implemented as a **Singleton**
- Ensures a single shared database connection across the application
- Prevents duplicated connections and inconsistent database state

---

## Technologies Used
- **Python 3**
- **SQLite** (`sqlite3`)
- **Logging** (`logging`)

No external libraries are required.

---

## Project Structure
All files are stored in a single directory for simplicity.
```text
exchange_cli/
├── main.py
├── cli_app.py
├── exchange_service.py
├── exchange_rate.py
├── conversion.py
├── database_manager.py
├── logger.py
├── requirements.txt
└── logs/
└── app.log
```

---

## System Architecture
The application follows a layered architecture:

- **CLI Layer (`cli_app.py`)**  
  Handles user input/output and menu display only.

- **Service Layer (`exchange_service.py`)**  
  Contains validation rules and business logic.

- **Database Layer (`database_manager.py`)**  
  Manages SQLite database access and schema.  
  Implemented as a **Singleton** to ensure one shared database connection.

- **Domain Models**  
  - `ExchangeRate` – exchange rate data  
  - `Conversion` – conversion transaction data  

---

## Database Schema
The application uses a local SQLite database named `exchange.db`.

### Table: `exchange_rate`
| Column | Type | Description |
|------|------|-------------|
| id | INTEGER | Primary key |
| base_currency | TEXT | Base currency code |
| target_currency | TEXT | Target currency code |
| rate | REAL | Exchange rate |
| updated_at | TEXT | UTC timestamp |

### Table: `conversion`
| Column | Type | Description |
|------|------|-------------|
| id | INTEGER | Primary key |
| amount | REAL | Original amount |
| converted_amount | REAL | Converted amount |
| rate_used | REAL | Rate applied |
| timestamp | TEXT | UTC timestamp |

---

## How to Run the Application

### Requirements
- Python 3.9 or higher
- No external libraries required

### Steps
1. Place all files in one folder
2. Open a terminal in that folder
3. Run the application:

```bash
python main.py
```

The database and tables are created automatically on first run.

---

## CLI Menu
```
1) View current exchange rate
2) Update exchange rate
3) Convert amount
0) Exit
```

---

## Scope and Limitations
- Supports only **one currency pair**
- Exchange rates are entered manually
- Command-line interface only
- No user authentication

---

## License
Educational use only.

---

## Author
Roxanne Prajapati  
Week 6 – Activity 8  
Currency Exchange CLI Application

