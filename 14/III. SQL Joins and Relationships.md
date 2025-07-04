
### **III. SQL Joins and Relationships**

---

#### **What Are Joins?**

A **JOIN** in SQL lets you **combine rows from two or more tables** based on a **related column**, usually using **foreign keys**. This is essential in **relational databases**, where data is split across multiple tables to avoid redundancy.

---

### **Why Use Joins?**

* Normalize data (avoid duplication)
* Connect related entities (e.g., Customers ↔ Orders)
* Prepare merged data for analysis or visualization
* Keep schema flexible and scalable

---

### **Key Join Types (with Visual Explanation)**

We’ll use two example tables:

#### **Customers Table**

| CustomerID | Name    |
| ---------- | ------- |
| 1          | Alice   |
| 2          | Bob     |
| 3          | Charlie |

#### **Orders Table**

| OrderID | CustomerID | OrderDate  |
| ------- | ---------- | ---------- |
| 101     | 1          | 2025-07-01 |
| 102     | 1          | 2025-07-02 |
| 103     | 2          | 2025-07-03 |

---

#### INNER JOIN

Returns only **matching rows** from both tables.

```sql
SELECT Customers.Name, Orders.OrderDate
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
```

**Result:**

| Name  | OrderDate  |
| ----- | ---------- |
| Alice | 2025-07-01 |
| Alice | 2025-07-02 |
| Bob   | 2025-07-03 |

**Diagram:**

```
Customers     Orders
   [1]  Alice   [101] CustID:1
   [2]  Bob     [102] CustID:1
   [3]  Charlie [103] CustID:2

        ⬇ INNER JOIN on CustomerID

      Only IDs present in BOTH → 1, 2
```

✅ *Charlie has no orders, so is excluded.*

---

#### LEFT JOIN (LEFT OUTER JOIN)

Returns **all rows from the left table** (Customers), and matched rows from the right table (Orders). If there's no match, the right side shows `NULL`.

```sql
SELECT Customers.Name, Orders.OrderDate
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
```

**Result:**

| Name    | OrderDate  |
| ------- | ---------- |
| Alice   | 2025-07-01 |
| Alice   | 2025-07-02 |
| Bob     | 2025-07-03 |
| Charlie | NULL       |

**Diagram:**

```
Customers     Orders
   [1] Alice    [101] CustID:1
   [2] Bob      [102] CustID:1
   [3] Charlie  [103] CustID:2

        ⬇ LEFT JOIN on CustomerID

      All Customers, even if no orders
```

✅ *Charlie is included even without matching orders.*

---

#### (Optional)  RIGHT JOIN and FULL JOIN

SQLite does **not** support `RIGHT JOIN` or `FULL OUTER JOIN` directly, but they exist in other RDBMS (PostgreSQL, SQL Server, etc.).

* **RIGHT JOIN**: Like LEFT JOIN, but starts from the right table
* **FULL OUTER JOIN**: Combines results from both sides, even if there’s no match on either side

---

###  **How This Helps in Python**

When you're analyzing data in **Pandas**, `JOINs` are equivalent to **`merge()`**:

```python
# Using pandas
import pandas as pd

customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

orders = pd.DataFrame({
    'OrderID': [101, 102, 103],
    'CustomerID': [1, 1, 2],
    'OrderDate': ['2025-07-01', '2025-07-02', '2025-07-03']
})

# INNER JOIN
merged_inner = pd.merge(customers, orders, on='CustomerID', how='inner')

# LEFT JOIN
merged_left = pd.merge(customers, orders, on='CustomerID', how='left')
```

---

### Key Concepts Recap

| Term            | Meaning                                                          |
| --------------- | ---------------------------------------------------------------- |
| **JOIN**        | Combines rows from multiple tables                               |
| **INNER JOIN**  | Only matching rows from both tables                              |
| **LEFT JOIN**   | All rows from left table, matched rows from right or NULL        |
| **RIGHT JOIN**  | All rows from right table, matched rows from left or NULL        |
| **FULL JOIN**   | All rows from both tables, NULL where no match                   |
| **Foreign Key** | A column in one table that references the primary key in another |
| **Aliasing**    | Use `AS` to rename columns or tables temporarily in a query      |

