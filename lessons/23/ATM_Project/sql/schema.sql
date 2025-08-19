--- name, surneame, email,.... PIN
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    email TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- account -  VISA, DEBIT, MAESTRO, N26, CURVE,...
CREATE TABLE IF NOT EXISTS Accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    balance REAL DEFAULT 0.0,
    card_type TEXT DEFAULT 'debit',
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);

-- my transaction table; where I store every trancation
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    merchant TEXT,
    amount REAL,
    transaction_type TEXT,
    datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);
