## **ATM Project Overview**

We will build a **fully functional ATM simulation** in Python that interacts with:

* **SQLite database** (for storing accounts, transactions, user info)
* **CSV log file** (for storing user actions: PIN entry, withdrawals, deposits, payments, etc.)
* **TXT error log file** (for exceptions and warnings)
* **Matplotlib & Pandas** for **data analysis and visualization**

---

## **Project Features**

### **1. Database Setup & Structure**

We’ll use **SQLite** (no external DB needed) with the following tables:

#### **SQL Schema**

```sql
CREATE TABLE Clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    email TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    balance REAL DEFAULT 0.0,
    card_type TEXT DEFAULT 'debit',
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);

CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    merchant TEXT,
    amount REAL,
    transaction_type TEXT,
    datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);
```

We’ll also have:

* **`db_manager.py`** → Handles all SQL queries & connections
* All queries will be parameterized to avoid **SQL injection**

---

### **2. Logging User Actions (CSV)**

* **Actions logged:**

  * Login attempts (success/failure)
  * PIN entry attempts
  * Deposits / Withdrawals
  * Balance checks
  * Payments (merchant, amount)
  * Changes in account settings

**CSV Format Example:**

```csv
timestamp,client_id,action,details
2025-07-29 10:12:45,1,login_success,Entered correct PIN
2025-07-29 10:15:02,1,withdraw,Amount: 200
```

---

### **3. Error Logging (TXT)**

* All runtime errors, database errors, and invalid input attempts will be stored in `error_log.txt`
* Example:

```
[2025-07-29 10:15:02] ERROR: Invalid withdrawal amount: -50
[2025-07-29 10:16:10] ERROR: Database connection lost
```

---

### **4. User Interaction (Console UI)**

**Menu Options:**

1. **Login** (PIN check)
2. **Check Balance**
3. **Deposit Money**
4. **Withdraw Money**
5. **Make Payment** (merchant, amount, card type)
6. **Settings**

   * Change PIN
   * Change personal info
7. **Transaction History**
8. **Data Insights & Visualizations**

   * Balance over time
   * Payments by merchant
   * Statistics: mean, min, max, median, std deviation
9. **Exit**

---

### **5. Data Wrangling & Visualization**

We will:

* Load **Transactions** table into Pandas
* Calculate:

  * Mean, Min, Max, Median, Std deviation of **transaction amounts**
  * Total spending per merchant
* Plot with **Matplotlib**:

  1. Balance over time line graph
  2. Payments per merchant bar chart
  3. Monthly spending trend

---

### **6. Input Validation & Error Handling**

* PIN: must be 4 digits
* Withdrawal: must be positive & ≤ current balance
* Deposit: must be positive
* Merchant name: must be non-empty string
* Amount: must be numeric and positive
* Card type: only `"debit"` or `"credit"`

---

### **7. Structure in Classes & Functions**

We will use **OOP** for clarity:

#### **Classes**

1. **`ATM`**

   * Manages login, menu navigation
2. **`Client`**

   * Stores user details, account links
3. **`Account`**

   * Deposit, withdraw, check balance
4. **`Transaction`**

   * Represents payments/withdrawals
5. **`DatabaseManager`**

   * Handles all SQL queries
6. **`Logger`**

   * Writes action logs (CSV) & error logs (TXT)
7. **`DataAnalyzer`**

   * Loads transactions into Pandas & produces statistics & plots

---

### **8. Extra Features for Realism**

* Multiple clients and accounts in the database
* Simulation mode:

  * Randomly generate transactions for testing
* Option to export transaction history to **CSV**
* Detect **suspicious transactions** (large withdrawals, multiple same-merchant payments in short time)
* Password/PIN hashing (using `hashlib` for security)

---

### **9. Example Workflow**

```
Welcome to Python ATM
Enter your PIN: ****
Login successful!

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Make Payment
5. Settings
6. View Statistics
7. Exit

> 3
Enter withdrawal amount: 200
Withdrawal successful. New balance: $800
Transaction saved to database and log file.
```

