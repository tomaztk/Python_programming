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
