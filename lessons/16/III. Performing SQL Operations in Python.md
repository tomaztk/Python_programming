

## **III. Performing SQL Operations in Python**

---

## Topics Covered:

* SQL Statements: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
* SQL Clauses: `WHERE`, `ORDER BY`, `LIMIT`
* Predicates for filtering data
* How to safely pass data to SQL queries (prevent SQL injection)

---

## **Key Concept**

You can perform all major SQL operations directly by sending SQL statements as strings from Python using **`cursor.execute()`**.

* SQL operations are dynamic — parameters are passed at runtime.
* Always use placeholders (`?`) in SQLite queries to prevent SQL injection.

---

## **Basic SQL Operations in Python**

---

###  **INSERT Operation (Adding Data)**

```python
def add_user(name, age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
    print(f"User '{name}' added successfully.")

# Example
add_user("David", 27)
add_user("Eve", 34)
```

---

###  **SELECT Operation (Reading Data)**

```python
def get_all_users():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
    return users

# Example
print("All Users:", get_all_users())
```

---

### **SELECT with WHERE Clause (Filtering Data)**

```python
def get_users_above_age(min_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE age > ?', (min_age,))
        users = cursor.fetchall()
    return users

# Example
print("Users older than 30:", get_users_above_age(30))
```

---

### **SELECT with ORDER BY and LIMIT Clauses**

```python
def get_youngest_users(limit):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY age ASC LIMIT ?', (limit,))
        users = cursor.fetchall()
    return users

# Example
print("Top 2 youngest users:", get_youngest_users(2))
```

---

### **UPDATE Operation (Modifying Data)**

```python
def update_user_age(name, new_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
        conn.commit()
    print(f"Updated '{name}' to age {new_age}.")

# Example
update_user_age("David", 29)
print(get_all_users())
```

---

### **DELETE Operation (Removing Data)**

```python
def delete_user(name):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE name = ?', (name,))
        conn.commit()
    print(f"User '{name}' deleted.")

# Example
delete_user("Eve")
print(get_all_users())
```

---

## **Summary of SQL Operations with Examples**

| Operation | SQL Syntax                                 | Python Example                                       |
| --------- | ------------------------------------------ | ---------------------------------------------------- |
| INSERT    | `INSERT INTO table (cols) VALUES (?, ?)`   | `cursor.execute('INSERT INTO...', (value1, value2))` |
| SELECT    | `SELECT * FROM table`                      | `cursor.execute('SELECT * FROM...')`                 |
| UPDATE    | `UPDATE table SET col = ? WHERE condition` | `cursor.execute('UPDATE table SET...')`              |
| DELETE    | `DELETE FROM table WHERE condition`        | `cursor.execute('DELETE FROM table WHERE...')`       |

---

## **Why Use Placeholders (`?`)**

* Protects against **SQL injection**
* Keeps queries readable and maintainable
* Avoids syntax errors with dynamic data

---

## **Practical Example — Combined Operations**

```python
def user_workflow_demo():
    add_user("Frank", 40)
    print("All users after adding Frank:", get_all_users())

    update_user_age("Frank", 41)
    print("All users after updating Frank:", get_all_users())

    delete_user("Frank")
    print("All users after deleting Frank:", get_all_users())

# Run the demo
user_workflow_demo()
```

---

##  **Recap:**

* You can fully control database data — insert, retrieve, update, delete — using SQL commands embedded in Python.
* Using **functions** for each operation keeps code modular and reusable.
* SQL clauses like `WHERE`, `ORDER BY`, and `LIMIT` make data querying powerful and flexible.
* Always commit your changes after modifying data.



