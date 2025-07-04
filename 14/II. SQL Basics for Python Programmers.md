### **II. SQL Basics for Python Programmers**

---

#### ** a. Introduction to CRUD Operations**

**CRUD** stands for:

| Operation  | SQL Keyword | Purpose                     |
| ---------- | ----------- | --------------------------- |
| **Create** | `INSERT`    | Add new records to a table  |
| **Read**   | `SELECT`    | Retrieve data from a table  |
| **Update** | `UPDATE`    | Modify existing records     |
| **Delete** | `DELETE`    | Remove records from a table |

---

####  **Examples of Each CRUD Operation**

Assume we have this `Customers` table:

```sql
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL
);
```

##### **1. SELECT – Read All Customers:**

```sql
SELECT * FROM Customers;
```

##### **2. INSERT – Add a New Customer:**

```sql
INSERT INTO Customers (Name, Email)
VALUES ('Alice Johnson', 'alice@example.com');
```

##### **3. UPDATE – Modify a Customer’s Email:**

```sql
UPDATE Customers
SET Email = 'alice_new@example.com'
WHERE Name = 'Alice Johnson';
```

##### **4. DELETE – Remove a Customer:**

```sql
DELETE FROM Customers
WHERE Name = 'Alice Johnson';
```

---

#### **Python Integration Tip**

In Python, you can use the built-in `sqlite3` library:

```python
import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()

# Insert example
cur.execute("INSERT INTO Customers (Name, Email) VALUES (?, ?)", ("John Doe", "john@example.com"))
conn.commit()

# Query example
cur.execute("SELECT * FROM Customers")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
```

You can also use **SQLAlchemy** for an object-relational mapping (ORM) approach.

---

### **b. Overview of SQL Predicates and Clauses**

SQL’s power comes from its **declarative syntax** and expressive **clauses**. What is this? 

WHat does **declarative** and **expressive** mean?

---

##### **Declarative Syntax** (vs. Imperative)

In SQL, **you describe *what* you want**, not **how** to get it.

* **Declarative**:
  SQL is *declarative*, meaning you write a query like:

  ```sql
  SELECT Name FROM Customers WHERE Email LIKE '%@example.com';
  ```

  This says: “Give me names of customers with emails ending in `@example.com`.”
  You don't tell the database *how* to search, loop, or filter — the database engine figures that out.

* **Imperative**:
  In contrast, languages like Python or JavaScript are *imperative* — you’d write a loop to manually process data.

**Summary**:
SQL focuses on *what* result you want, not *how* to compute it. The database engine handles the logic.

---

##### **Expressive Clauses**

**Clauses** are the building blocks of SQL queries — they let you:

| Clause     | What it does                         |
| ---------- | ------------------------------------ |
| `SELECT`   | Choose which columns to return       |
| `FROM`     | Choose which table(s) to query       |
| `WHERE`    | Filter rows based on conditions      |
| `ORDER BY` | Sort the results                     |
| `GROUP BY` | Group rows for aggregation           |
| `HAVING`   | Filter groups (after `GROUP BY`)     |
| `JOIN`     | Combine rows from multiple tables    |
| `LIMIT`    | Restrict the number of rows returned |

These **clauses make SQL very powerful and readable** — you can construct rich queries with just a few lines of code.

---

### Example: Declarative and Expressive

```sql
SELECT CustomerID, COUNT(*) AS TotalOrders
FROM Orders
WHERE OrderDate >= '2025-01-01'
GROUP BY CustomerID
HAVING COUNT(*) > 5
ORDER BY TotalOrders DESC;
```

This one line of SQL:

* filters orders by date
* groups them by customer
* counts how many orders each customer made
* filters groups to only include those with more than 5 orders
* sorts results by most orders

All without writing a single loop or manual filter!







---

#### ** WHERE – Filter Records**

Select all orders made by Customer ID 1:

```sql
SELECT * FROM Orders WHERE CustomerID = 1;
```

---

#### ** ORDER BY – Sort Results**

Sort customers alphabetically:

```sql
SELECT * FROM Customers ORDER BY Name ASC;
```

Sort customers by most recent email update (if timestamp column exists):

```sql
SELECT * FROM Customers ORDER BY LastUpdated DESC;
```

---

#### ** GROUP BY – Aggregate Data**

Find how many orders each customer has made:

```sql
SELECT CustomerID, COUNT(*) AS TotalOrders
FROM Orders
GROUP BY CustomerID;
```

You can also use `HAVING` to filter aggregated results:

```sql
SELECT CustomerID, COUNT(*) AS TotalOrders
FROM Orders
GROUP BY CustomerID
HAVING COUNT(*) > 2;
```

---

### **Key SQL Concepts**

| Concept                 | Description                                                          |
| ----------------------- | -------------------------------------------------------------------- |
| **Clause**              | A keyword-driven part of a SQL statement (e.g., `WHERE`, `ORDER BY`) |
| **Predicate**           | A condition used in `WHERE`, `HAVING`, etc., to filter rows          |
| **Wildcard**            | `*` selects all columns, `%` used in `LIKE` for pattern matching     |
| **Aggregate Functions** | `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()` for grouping data      |
| **Joins**               | Combine rows from two or more tables based on related columns        |


