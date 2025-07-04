### **LESSON 14: INTRODUCTION TO SQL FOR PYTHON DEVELOPERS**

---

### **1. Foundations of Relational Databases**

* **Explanation:**
  Relational databases store data in **tables (relations)**, where each table consists of **rows** (records) and **columns** (fields). Tables can relate to each other via **foreign keys**, allowing for complex data models.

* **Demo/Example:**
  Display a simple example of two related tables:

  ```sql
  -- Customers table
  CREATE TABLE Customers (
      CustomerID INTEGER PRIMARY KEY,
      Name TEXT,
      Email TEXT
  );

  -- Orders table
  CREATE TABLE Orders (
      OrderID INTEGER PRIMARY KEY,
      OrderDate TEXT,
      CustomerID INTEGER,
      FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
  );
  ```

---

#### **2. SQL Basics for Python Programmers**

##### **a. Introduction to CRUD Operations**

* **Explanation:**
  CRUD stands for Create, Read, Update, Delete — the four basic functions for persistent storage.

* **Examples:**

  * **SELECT (Read)**
    Retrieve all customers:

    ```sql
    SELECT * FROM Customers;
    ```
  * **INSERT (Create)**
    Add a new customer:

    ```sql
    INSERT INTO Customers (Name, Email)
    VALUES ('Alice Johnson', 'alice@example.com');
    ```
  * **UPDATE (Modify)**
    Update a customer's email:

    ```sql
    UPDATE Customers
    SET Email = 'alice_new@example.com'
    WHERE Name = 'Alice Johnson';
    ```
  * **DELETE (Remove)**
    Delete a customer:

    ```sql
    DELETE FROM Customers
    WHERE Name = 'Alice Johnson';
    ```

* **Python Integration Note:**
  These operations can later be performed within Python using libraries like `sqlite3` or `SQLAlchemy`.

---

##### **b. Overview of SQL Predicates and Clauses**

* **Explanation & Examples:**

  * **WHERE** – Filters rows:

    ```sql
    SELECT * FROM Orders WHERE CustomerID = 1;
    ```
  * **ORDER BY** – Sorts results:

    ```sql
    SELECT * FROM Customers ORDER BY Name ASC;
    ```
  * **GROUP BY** – Aggregates data:

    ```sql
    SELECT CustomerID, COUNT(*) AS TotalOrders
    FROM Orders
    GROUP BY CustomerID;
    ```

* **Demo Tip:**
  Use an online SQL playground (like SQLite online or DB Fiddle) to let learners try modifying queries live.

---

#### **3. SQL Joins and Relationships**

* **Explanation:**
  Joins allow you to combine rows from two or more tables based on a related column.

* **Types of Joins and Examples:**

  * **INNER JOIN**

    ```sql
    SELECT Customers.Name, Orders.OrderDate
    FROM Customers
    INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
    ```
  * **LEFT JOIN**

    ```sql
    SELECT Customers.Name, Orders.OrderDate
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
    ```

* **Use Case:**
  These joins become essential when you need to prepare data in Python for analytics or visualizations.

---

#### **4. Hands-On Practice**

* **Activity:**
  Provide learners with a sample SQLite database file or online playground access.

* **Tasks:**

  1. Write queries to retrieve customer names with orders.
  2. Find customers without any orders (using `LEFT JOIN` and `WHERE OrderID IS NULL`).
  3. Count orders per customer using `GROUP BY`.

* **Integration with Python:**

  * Show a brief snippet of how Python retrieves SQL data:

    ```python
    import sqlite3

    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customers;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()
    ```

---

### **Homework**

**Task:**
Write a series of SQL queries that:

1. Retrieve all customer names who have placed more than one order.
2. Insert a new order for a given customer.
3. Update an order's date.
4. Delete an order by ID.

**Documentation Requirement:**
For each query, explain:

* What the query does
* Why it would be useful in a real application
* How it could be integrated with Python (e.g., `sqlite3`, `pandas.read_sql_query`)

**Bonus:**
Export a SQL query result to a `.csv` using Python, e.g.:

```python
import pandas as pd
df = pd.read_sql_query("SELECT * FROM Orders", conn)
df.to_csv('orders.csv', index=False)
```

---

Let me know if you'd like a sample SQLite database file or a Jupyter Notebook companion for this lesson.
