## **LESSON 16: INTEGRATING SQL WITH PYTHON**

**Tools Required:** Python 3.x, SQLite (or PostgreSQL/MySQL), SQLAlchemy, Pandas

---

###  **Recap: Previous Lesson**

* Quick review of file I/O, data structures, or previous data handling modules.
* Introduce the motivation for using SQL with Python (e.g., persistent data storage, querying capabilities).

---

### **Using Python Packages to Connect to SQL Databases**

We'll use **`sqlite3`** and **`SQLAlchemy`** (high-level ORM) to demonstrate database integration.

#### **Example 1: Using `sqlite3`**

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
conn.commit()
conn.close()
```

#### **Example 2: Using `SQLAlchemy`**

```python
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine('sqlite:///example.db')
metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)

metadata.create_all(engine)
```

---

###  **SQL Statements in Python**

We'll cover:

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`

#### **Example 3: INSERT and SELECT**

```python
# Using sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)
conn.close()
```

---

###  **SQL Predicates, Joins, and Clauses**

#### **SQL Predicates:**

```sql
SELECT * FROM users WHERE age > 25;
```

#### **Example 4: INNER JOIN**

```python
# Assume another table: orders(user_id, product)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')
conn.commit()

cursor.execute("INSERT INTO orders (user_id, product) VALUES (?, ?)", (1, 'Book'))
conn.commit()

cursor.execute('''
    SELECT users.name, orders.product 
    FROM users 
    JOIN orders ON users.id = orders.user_id
''')

print(cursor.fetchall())
```

---

###  **Embedding SQL in Python Functions and Pandas**

#### **Example 5: Encapsulating SQL in Functions**

```python
def get_users_above_age(min_age):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE age > ?", (min_age,))
        return cursor.fetchall()
```

#### **Example 6: Using Pandas with SQL**

```python
import pandas as pd

with sqlite3.connect('example.db') as conn:
    df = pd.read_sql_query("SELECT * FROM users", conn)

print(df)
```

---

###  **Hands-On Demo: Transactional Update and Result Retrieval**

#### **Example 7: Transactional Update**

```python
def update_user_age(user_id, new_age):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchall()

print(update_user_age(1, 35))
```

---

###  **Homework Assignment**

> **Goal:** Develop a Python application that connects to a database, performs a series of SQL operations (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), and processes the results with Pandas.

#### **Homework Requirements**

* Connect to a database using either `sqlite3` or `SQLAlchemy`.
* Create two tables (e.g., `customers` and `orders`).
* Insert data using Python functions.
* Update and delete records based on conditions.
* Fetch and process results with Pandas.
* Include commentary on how SQL integration benefits data manipulation.

#### **Extra Tips:**

* Use transactions and handle exceptions.
* Show intermediate steps using Pandas DataFrames.
* Document your code with comments and/or markdown if using Jupyter Notebook.

