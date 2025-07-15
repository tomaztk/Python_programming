# **LESSON 17: INTEGRATING SQL WITH PYTHON (Solution)**

## **Part 1: Core SQL Assignments (1-10)**

### 1. Create Database and Table

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
);
```

---

### 2. Insert Data into Table

```sql
INSERT INTO employees (name, department, salary) VALUES
('John Doe', 'HR', 55000),
('Jane Smith', 'IT', 70000),
('Mike Brown', 'Finance', 48000),
('Sara Wilson', 'IT', 65000),
('Tom Clark', 'HR', 52000);
```

---

###  3. SELECT All Records

```sql
SELECT * FROM employees;
```

---

### 4. SELECT with WHERE Clause

```sql
SELECT * FROM employees WHERE salary > 50000;
```

---

### 5. Update a Record

```sql
UPDATE employees SET salary = 75000 WHERE id = 2;
```

---

### 6. Delete a Record

```sql
DELETE FROM employees WHERE id = 3;
```

---

### 7. ORDER BY Clause

```sql
SELECT * FROM employees ORDER BY salary DESC;
```

---

### 8. SELECT with LIKE Operator

```sql
SELECT * FROM employees WHERE name LIKE 'J%';
```

---

### 9. COUNT Aggregate Function

```sql
SELECT COUNT(*) AS total_employees FROM employees;
```

---

### 10. AVG with GROUP BY

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

---

##  **Part 2: SQL with Python (sqlite3) Assignments (11-20)**

We’ll use this standard connection setup for Python assignments:

```python
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()
```

---

### 11. Connect to SQLite in Python

```python
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()
print("Connected successfully!")
```

---

### 12. Create Table if Not Exists

```python
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    budget REAL
)
''')
conn.commit()
```

---

### 13. Insert Multiple Records with `executemany()`

```python
projects_data = [
    ('Website Redesign', 10000),
    ('Mobile App', 25000),
    ('Cloud Migration', 15000)
]

cursor.executemany('''
INSERT INTO projects (name, budget) VALUES (?, ?)
''', projects_data)
conn.commit()
```

---

### 14.  SELECT Query and Fetch Results

```python
cursor.execute('SELECT * FROM employees')
for row in cursor.fetchall():
    print(row)
```

---

### 15. Update Data with Variables

```python
emp_id = 1
new_salary = 60000
cursor.execute('''
UPDATE employees SET salary = ? WHERE id = ?
''', (new_salary, emp_id))
conn.commit()
```

---

### 16. Delete Record with WHERE using Parameters

```python
emp_id_to_delete = 5
cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id_to_delete,))
conn.commit()
```

---

### 17. Fetch Results with Filtering

```python
department = 'IT'
cursor.execute('SELECT * FROM employees WHERE department = ?', (department,))
for row in cursor.fetchall():
    print(row)
```

---

### 18. Handle SQL Exceptions in Python

```python
try:
    cursor.execute('SELECT * FROM non_existing_table')
except sqlite3.Error as e:
    print("An error occurred:", e)
```

---

### 19. Commit Transactions and Close Connection

```python
conn.commit()
conn.close()
print("Connection closed.")
```

---

### 20. Bonus Challenge: Create a Simple Report

```python
cursor.execute('''
SELECT department, SUM(salary) as total_salary
FROM employees
GROUP BY department
''')
for row in cursor.fetchall():
    print(f"Department: {row[0]}, Total Salary: {row[1]}")
```

---
