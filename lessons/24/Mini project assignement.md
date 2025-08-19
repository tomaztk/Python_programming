

#  Car Rental System – Mini assignment for certificate

---

## **1. Goals of the Assignment**

Create a realistic **Car Rental System** that:

* Manages **multiple clients**, **multiple cars**, **rental and return transactions**
* Stores data in an **SQLite database**
* Logs **user actions** to a **CSV file**
* Logs **errors** to a **TXT file**
* Implements **input validation** and **error handling**
* Performs **data wrangling** to generate **client-specific statistics** and **visualizations**
* Is structured using **classes**, **methods**, and **proper data types**

---

## **2. Core Functionalities**

### 1. **Client Login / Registration**

* **Login** with email or client ID
* Validate inputs
* Limit failed login attempts
* Allow new client registration with:

  * Name
  * Email
  * Phone Number
  * Driver’s license (optional)
* Store client info in the DB

---

### 2. **View Available Cars**

* List all cars not currently rented
* Filter by category, price, or model
* Fetch from DB with proper queries

---

### 3. **Rent a Car**

* Input: Car ID, rental days
* Validation: Car must be available, days > 0
* Update:

  * Car status → rented
  * Insert rental record in `rentals` table
* Log the rental action in CSV
* Calculate cost = `daily_rate * days`

---

### 4. **Return a Car**

* Input: Rental ID or Car ID
* Calculate:

  * Total days
  * Late fees (if any)
* Update:

  * Car status → available
  * Rental record → completed
* Log the return

---

### 5. **View My Rentals**

* Show current and past rentals
* Sort by date, car, status

---

### 6. **Update Client Settings**

* Change name, phone, email
* Update DB records
* Log each action

---

### 7. **View Statistics (Per Client)**

* Show:

  * Total cars rented
  * Average rental duration
  * Most rented car
  * Total amount spent
* Visuals using **Matplotlib/Seaborn**:

  * Rental durations over time
  * Spending trend by month
  * Pie chart of rental categories

---

## **3. Database Schema (SQLite)**

### `clients`

| id | name | email | phone | registration\_date |

### `cars`

| id | model | brand | category | daily\_rate | is\_rented (bool) |

### `rentals`

\| id | client\_id | car\_id | start\_date | end\_date | total\_cost | status |

---

## **4. File Logging**

###  User Actions – `actions_log.csv`

```csv
timestamp,client_id,action,details
2025-08-06 12:45:00,CL001,"RENT","Car ID: C003 for 3 days"
```

###  Error Logs – `error_log.txt`

```
[2025-08-06 13:15:21] ERROR: Invalid input for rental days. Must be integer > 0.
```

---

## **5. Input Validation & Error Handling**

* Email format validation
* Check car availability
* Rental period > 0
* Catch all DB errors, file errors, etc.
* Centralized error logging

---

## **6. OOP Structure**

### Classes

```python
class Client:
    def login()
    def register()
    def update_profile()

class Car:
    def list_available()
    def update_status()

class Rental:
    def rent_car()
    def return_car()
    def calculate_cost()
    def get_statistics()

class Database:
    def connect()
    def execute_query()
    def fetch()

class Logger:
    def log_action()
    def log_error()
```

---

## **7. Data Wrangling & Visualization**

Use **Pandas + Matplotlib/Seaborn**:

* Load rentals per client
* Group by:

  * Car
  * Month
  * Duration
* Visualize:

  * Total amount spent
  * Popular cars
  * Rentals per month

---

### **. Optional Enhancements**

* Admin panel to add/remove cars
* Car availability calendar
* Export client invoices to PDF
* Tiered membership (Gold, Silver, etc.)



## 8. **Submission Instructions**
****
###  **What to Submit**

You must submit a **single `.zip` file** or a **folder** containing:

* All your **Python source files** (`.py`)
* The **SQLite database file**: `data.db`
* Log files:

  * `actions_log.csv`
  * `error_log.txt`
* Optional: statistics images in `/visuals` folder
* A `README.txt` or `README.md` file with:

  * Short usage instructions
  * Required libraries
  * Entry point (e.g., `main.py`)

---

### **File Naming Convention**

* Your `.zip` file or folder must be named:

  ```
  yourname_yoursurname.zip
  ```

  Example: `alex_smith.zip`

### **File Organization**

It includes:

* `main.py` – Entry point
* `modules/` – Python classes for `Client`, `Car`, `Rental`, `Database`, `Logger`
* `database/data.db` – Empty SQLite database
* `logs/` – Placeholder for action and error logs
* `visuals/` – Placeholder for charts
* `README.md` – Usage instructions


---

### **How to Submit**

 Upload the `.zip` file to the **LMS platform**

**12.08.2025, 23:59 (EOD)**
Late submissions **will not be accepted** unless Aneta's / Bojan's approval is given.

