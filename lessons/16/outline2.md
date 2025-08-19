
#  **LESSON 16: INTEGRATING SQL WITH PYTHON**

**Duration:** 2 hours
**Objective:** Learn how to integrate SQL with Python for robust, efficient, and persistent data management.

---

##  **SECTION 1: Introduction and Database Setup**

###  Topics Covered:

* Recap of previous lesson (data handling, files, or structures)
* Introduction to relational databases and SQL
* Using Python to connect with databases

###  Key Concept:

A database allows structured storage, querying, and updating of large datasets. SQL is the language to interact with databases; Python bridges that interaction.

###  Tools:

* `sqlite3` (built-in)
* `SQLAlchemy` (optional for abstraction)
* `pandas` (for data manipulation)

###  Code Demo: Creating a SQLite Database

```python
import sqlite3

# Create a new database file
conn = sqlite3.connect('lesson16.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

conn.commit()
conn.close()
```

---

##  **SECTION 2: Performing SQL Operations in Python**

###  Topics Covered:

* SQL Statements: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
* Predicates and Clauses: `WHERE`, `ORDER BY`, etc.

###  Explanation:

Each SQL statement can be sent as a string to the database through Python. Parameters should be safely passed using placeholders to avoid SQL injection.

###  Code Demo: Basic Operations

```python
conn = sqlite3.connect('lesson16.db')
cursor = conn.cursor()

# INSERT
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

# SELECT
cursor.execute("SELECT * FROM users")
print("All Users:", cursor.fetchall())

# UPDATE
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))

# DELETE
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))

conn.commit()
conn.close()
```

---

##  **SECTION 3: Advanced Queries and Integration with Functions & Pandas**

###  Topics Covered:

* SQL Joins (e.g., INNER JOIN)
* Embedding SQL in reusable Python functions
* Working with query results using Pandas

###  Code Demo: JOIN and Functions

```python
# Create orders table
conn = sqlite3.connect('lesson16.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 28))
cursor.execute("INSERT INTO orders (user_id, product) VALUES (?, ?)", (1, "Laptop"))
conn.commit()

# JOIN
cursor.execute('''
SELECT users.name, orders.product
FROM users
JOIN orders ON users.id = orders.user_id
''')

print("Join Result:", cursor.fetchall())
conn.close()
```

###  Code Demo: Function + Pandas Integration

```python
import pandas as pd

def get_users_dataframe():
    with sqlite3.connect('lesson16.db') as conn:
        return pd.read_sql_query("SELECT * FROM users", conn)

df = get_users_dataframe()
print(df)
```

---

##  **SECTION 4: Hands-On Practice + Homework Assignment**

### Hands-On Task: Transactional Update and Fetch

```python
def update_age_and_fetch(user_id, new_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchall()

print(update_age_and_fetch(1, 35))
```

---

###  Homework Assignment

**Objective:** Build a complete Python mini-app that connects to a database and demonstrates SQL integration.

####  Requirements:

1. Connect to a database (SQLite or SQLAlchemy).
2. Create at least two tables (e.g., `customers`, `orders`).
3. Implement:

   * `INSERT`, `SELECT`, `UPDATE`, `DELETE` SQL operations.
   * At least one SQL `JOIN`.
   * One transactional change that is fetched in Python.
4. Use **Pandas** to:

   * Fetch and display the final results.
   * Optionally filter or sort the output.
5. Add **code comments** or markdown cells explaining:

   * Why SQL integration is powerful for structured data.
   * How each SQL command maps to Python logic.

