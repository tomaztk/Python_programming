### **IV. Hands-On Practice**

---

#### **Objective: Learn by Doing**

SQL is best learned through **hands-on practice**. In this section, learners will:

* Interact with real data using SQL queries
* Understand joins, filters, and aggregations
* See how SQL connects to Python programs

---

### **Setup: Use SQLite (No Installation Required)**

To make this accessible:

* Use [SQLite Online](https://sqliteonline.com/) or [DB Fiddle](https://www.db-fiddle.com/)
* Or, run it locally with Python’s `sqlite3` (built-in)

---

### **Create Sample Database & Tables**

Let’s create a basic schema with `Customers`, `Orders`, and `Products`.

```sql
-- Create Customers table
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE
);

-- Create Orders table
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT NOT NULL,
    CustomerID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Insert sample customers
INSERT INTO Customers (Name, Email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Carol White', 'carol@example.com');

-- Insert sample orders
INSERT INTO Orders (OrderDate, CustomerID) VALUES
('2025-07-01', 1),
('2025-07-02', 1),
('2025-07-03', 2);
```

---

### **Practice Tasks**

Learners can now write SQL queries based on the schema above.

---

#### Task 1: Retrieve Customer Names with Orders

```sql
SELECT Customers.Name, Orders.OrderDate
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
```

> *This gets only those customers who have placed at least one order.*

---

#### Task 2: Find Customers Without Orders

```sql
SELECT Customers.Name
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderID IS NULL;
```

> *This returns customers who don’t have any orders. Useful for identifying inactive users.*

---

#### Task 3: Count Orders Per Customer

```sql
SELECT Customers.Name, COUNT(Orders.OrderID) AS OrderCount
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerID;
```

> *Combines join with aggregation — helps find total orders per customer.*

---

### **Python Integration: Accessing SQL from Python**

Once a database is created (e.g., `sample.db`), you can run SQL queries directly in Python.

#### Example Python Script

```python
import sqlite3

# Connect to the SQLite database (creates file if it doesn’t exist)
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT,
    Email TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT,
    CustomerID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
""")

# Insert data (optional if already exists)
cursor.execute("INSERT OR IGNORE INTO Customers (CustomerID, Name, Email) VALUES (1, 'Alice Johnson', 'alice@example.com')")
cursor.execute("INSERT OR IGNORE INTO Customers (CustomerID, Name, Email) VALUES (2, 'Bob Smith', 'bob@example.com')")
cursor.execute("INSERT OR IGNORE INTO Orders (OrderID, OrderDate, CustomerID) VALUES (101, '2025-07-01', 1)")

# Run a SELECT query
cursor.execute("""
SELECT Customers.Name, Orders.OrderDate
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
""")

# Fetch and display results
results = cursor.fetchall()
for row in results:
    print(row)

conn.close()
```

>  *This script creates a small local database, adds data, and runs a join query — great for practice and prototyping!*

---

### **Bonus Assignments**

1. Get the most recent order for each customer
2. Count how many customers placed multiple orders
3. Add a `Products` table and JOIN it to orders
4. Filter orders by date range (e.g., July 2025)
5. Export query results to CSV in Python

---



