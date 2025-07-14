
#  **LESSON 16: INTEGRATING SQL WITH PYTHON**

## **II. Introduction and Database Setup**

## Topics Covered:

* Recap of previous lesson (data handling, files, or structures)
* Introduction to relational databases and SQL
* Using Python to create and connect to SQLite databases

---

## **Key Concept**

A **relational database** is a structured way to store data in tables (rows & columns) with relationships between them.
**SQL (Structured Query Language)** is the standard way to interact with databases: insert, retrieve, update, and delete data.
Python’s **`sqlite3` module** allows you to handle a relational database **without leaving Python**, perfect for small to medium apps.

---

##  **Tool of Choice: `sqlite3`**

* Built into Python (no installation required)
* Lightweight, file-based
* SQL standard support
* Suitable for demos, small apps, and prototyping

---

## **1. Creating a SQLite Database and Table**


## **How SQLite Creates a Database**

```python
import sqlite3

# This will create 'lesson16.db' in the same folder if it doesn't exist
conn = sqlite3.connect('lesson16.db')
print("Database 'lesson16.db' created or opened successfully.")
conn.close()
```

>  **If the file `lesson16.db` exists → it connects to it.
>  If it doesn't exist → SQLite creates it.**


## **How to create a Table if Not Exists**

```python
def initialize_database():
    conn = sqlite3.connect('lesson16.db')
    cursor = conn.cursor()
    
    # Create 'users' table if it doesn't exist already
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized and 'users' table ensured.")

# Initialize the database and table
initialize_database()
```

---
### Together in 4 steps with connection open and close


```python
import sqlite3

#  Connect to (or create) a database file
conn = sqlite3.connect('lesson16.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and 'users' table created successfully.")
```

### **What this code does:**

* **Connects** to `lesson16.db` (creates if not existing)
* **Creates** a `users` table with:

  * `id` as an auto-incrementing primary key
  * `name` as text (non-null)
  * `age` as integer (non-null)
* **Commits** changes
* **Closes** the connection

---

## **2. Repeated Connections — Safe Way with Context Manager**

```python
def create_user(name, age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
    print(f"User '{name}' added successfully.")

# Example Usage
create_user("Alice", 30)
create_user("Bob", 25)
```

### **Why use `with` block?**

* Automatically closes the connection even if an error occurs.
* Safer and cleaner than manual close.

---

## **3. Reading Data from the Table**

```python
def fetch_all_users():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
    return users

print(fetch_all_users())
```

---

## **Summary of Basic Database Operations**

| Operation        | Python Example                       |
| ---------------- | ------------------------------------ |
| Create Table     | `cursor.execute('CREATE TABLE...')`  |
| Insert Data      | `cursor.execute('INSERT INTO...')`   |
| Select Data      | `cursor.execute('SELECT * FROM...')` |
| Commit Changes   | `conn.commit()`                      |
| Close Connection | `conn.close()` or use `with` block   |

---

## **Important: Simple Error Handling Example**

```python
def insert_user_safe(name, age):
    try:
        with sqlite3.connect('lesson16.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
            conn.commit()
        print(f"Inserted user: {name}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

insert_user_safe("Charlie", 40)
```

---

##  **Recap:**

* You can **fully control a SQLite database directly from Python**.
* **Connection → Cursor → Execute SQL → Commit → Close** is the typical workflow.
* Using functions makes database operations reusable and clean.
* Using **parameterized queries** (`?` placeholders) protects against SQL injection.
* Context managers (`with` block) ensure safe connection handling.


