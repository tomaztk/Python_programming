
## **ATM Project – Full Code Skeleton**

### ** `db_manager.py` – Database Manager**

```python
import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path="data/atm.db"):
        os.makedirs("data", exist_ok=True)
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS Clients (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                pin TEXT NOT NULL,
                email TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """)
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS Accounts (
                account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER NOT NULL,
                balance REAL DEFAULT 0.0,
                card_type TEXT DEFAULT 'debit',
                FOREIGN KEY (client_id) REFERENCES Clients(client_id)
            )
            """)
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS Transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER NOT NULL,
                merchant TEXT,
                amount REAL,
                transaction_type TEXT,
                datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
            )
            """)

    def add_client(self, name, pin, email):
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO Clients (name, pin, email) VALUES (?, ?, ?)",
                (name, pin, email)
            )
            return cur.lastrowid

    def add_account(self, client_id, balance=0.0, card_type="debit"):
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO Accounts (client_id, balance, card_type) VALUES (?, ?, ?)",
                (client_id, balance, card_type)
            )
            return cur.lastrowid

    def get_client_by_pin(self, pin):
        cur = self.conn.execute("SELECT * FROM Clients WHERE pin=?", (pin,))
        return cur.fetchone()

    def get_account_by_client(self, client_id):
        cur = self.conn.execute("SELECT * FROM Accounts WHERE client_id=?", (client_id,))
        return cur.fetchone()

    def update_balance(self, account_id, new_balance):
        with self.conn:
            self.conn.execute(
                "UPDATE Accounts SET balance=? WHERE account_id=?",
                (new_balance, account_id)
            )

    def add_transaction(self, account_id, merchant, amount, transaction_type):
        with self.conn:
            self.conn.execute(
                "INSERT INTO Transactions (account_id, merchant, amount, transaction_type) VALUES (?, ?, ?, ?)",
                (account_id, merchant, amount, transaction_type)
            )

    def get_transactions(self, account_id):
        cur = self.conn.execute("SELECT * FROM Transactions WHERE account_id=?", (account_id,))
        return cur.fetchall()
```

---

### ** `logger.py` – Action & Error Logger**

```python
import csv
import os
from datetime import datetime

class Logger:
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        self.action_log = "logs/actions_log.csv"
        self.error_log = "logs/error_log.txt"

    def log_action(self, client_id, action, details=""):
        with open(self.action_log, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), client_id, action, details])

    def log_error(self, error_message):
        with open(self.error_log, "a") as f:
            f.write(f"{datetime.now()} - ERROR: {error_message}\n")
```

---

### ** `data_analyzer.py` – Data Analysis & Plots**

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

class DataAnalyzer:
    def __init__(self, db_manager):
        self.db = db_manager
        os.makedirs("plots", exist_ok=True)

    def _load_transactions_df(self, account_id):
        rows = self.db.get_transactions(account_id)
        df = pd.DataFrame(rows, columns=["id", "account_id", "merchant", "amount", "type", "datetime"])
        df["datetime"] = pd.to_datetime(df["datetime"])
        return df

    def plot_balance_over_time(self, account_id):
        df = self._load_transactions_df(account_id)
        df["balance"] = df["amount"].cumsum()
        plt.figure()
        plt.plot(df["datetime"], df["balance"], marker="o")
        plt.title("Balance Over Time")
        plt.savefig("plots/balance_over_time.png")

    def plot_payments_by_merchant(self, account_id):
        df = self._load_transactions_df(account_id)
        merchant_totals = df.groupby("merchant")["amount"].sum()
        plt.figure()
        merchant_totals.plot(kind="bar")
        plt.title("Payments by Merchant")
        plt.savefig("plots/payments_by_merchant.png")

    def print_statistics(self, account_id):
        df = self._load_transactions_df(account_id)
        print("Mean:", df["amount"].mean())
        print("Min:", df["amount"].min())
        print("Max:", df["amount"].max())
        print("Median:", df["amount"].median())
        print("Std Dev:", df["amount"].std())
```

---

### ** `atm.py` – ATM Logic**

```python
class ATM:
    def __init__(self, db_manager, logger, data_analyzer):
        self.db = db_manager
        self.logger = logger
        self.analyzer = data_analyzer

    def login(self):
        for _ in range(3):
            pin = input("Enter your 4-digit PIN: ")
            if not (pin.isdigit() and len(pin) == 4):
                print("Invalid PIN format!")
                continue
            client = self.db.get_client_by_pin(pin)
            if client:
                print(f"Welcome {client[1]}!")
                account = self.db.get_account_by_client(client[0])
                return client, account
            else:
                print("PIN not found.")
        print("Too many failed attempts.")
        return None, None

    def main_menu(self, client, account):
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Make Payment")
            print("5. View Statistics")
            print("6. Exit")

            choice = input("Select option: ")
            if choice == "1":
                self.check_balance(account)
            elif choice == "2":
                self.deposit_money(account)
            elif choice == "3":
                self.withdraw_money(account)
            elif choice == "4":
                self.make_payment(account)
            elif choice == "5":
                self.view_statistics(account)
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

    def check_balance(self, account):
        print(f"Your balance is: {account[2]:.2f}")
        self.logger.log_action(account[1], "CHECK_BALANCE")

    def deposit_money(self, account):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Deposit must be positive.")
            new_balance = account[2] + amount
            self.db.update_balance(account[0], new_balance)
            self.db.add_transaction(account[0], "Deposit", amount, "deposit")
            self.logger.log_action(account[1], "DEPOSIT", amount)
            print("Deposit successful.")
            account = self.db.get_account_by_client(account[1])
        except Exception as e:
            self.logger.log_error(str(e))
            print("Error during deposit.")

    def withdraw_money(self, account):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0 or amount > account[2]:
                raise ValueError("Invalid withdrawal amount.")
            new_balance = account[2] - amount
            self.db.update_balance(account[0], new_balance)
            self.db.add_transaction(account[0], "ATM Withdrawal", -amount, "withdrawal")
            self.logger.log_action(account[1], "WITHDRAW", amount)
            print("Withdrawal successful.")
            account = self.db.get_account_by_client(account[1])
        except Exception as e:
            self.logger.log_error(str(e))
            print("Error during withdrawal.")

    def make_payment(self, account):
        try:
            merchant = input("Enter merchant name: ")
            amount = float(input("Enter amount: "))
            if amount <= 0 or amount > account[2]:
                raise ValueError("Invalid payment amount.")
            new_balance = account[2] - amount
            self.db.update_balance(account[0], new_balance)
            self.db.add_transaction(account[0], merchant, -amount, "payment")
            self.logger.log_action(account[1], "PAYMENT", f"{merchant}:{amount}")
            print("Payment successful.")
            account = self.db.get_account_by_client(account[1])
        except Exception as e:
            self.logger.log_error(str(e))
            print("Error during payment.")

    def view_statistics(self, account):
        self.analyzer.print_statistics(account[0])
        self.analyzer.plot_balance_over_time(account[0])
        self.analyzer.plot_payments_by_merchant(account[0])
        print("Statistics & plots generated.")
```

---

### **`main.py` – Entry Point**

```python
from db_manager import DatabaseManager
from logger import Logger
from data_analyzer import DataAnalyzer
from atm import ATM

if __name__ == "__main__":
    db = DatabaseManager()
    logger = Logger()
    analyzer = DataAnalyzer(db)
    atm = ATM(db, logger, analyzer)

    # Optional: Add a test client
    if not db.get_client_by_pin("1234"):
        client_id = db.add_client("John Doe", "1234", "john@example.com")
        db.add_account(client_id, 500.0, "debit")

    client, account = atm.login()
    if client:
        atm.main_menu(client, account)
```

---

