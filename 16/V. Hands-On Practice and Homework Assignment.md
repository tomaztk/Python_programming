
#  **V. Hands-On Practice and Homework Assignment**

---

##  **Purpose of this Section**

* Practice transactional SQL operations directly in Python
* Capture and verify affected rows after changes
* Encourage building a real-life mini-application with SQL and Python
* Use **Pandas** for data presentation and filtering

---

##  **Key Concept: Transactions & Fetching Results**

* A **transaction** groups one or more SQL operations together.
* You `COMMIT` to apply changes permanently.
* After an update, you often want to **fetch the affected data** for validation or further processing.
* This pattern is critical for building reliable applications.

---

## **Hands-On Demo: Transactional Update and Fetch**

### Function Example — Update and Fetch

```python
def update_user_age_and_get(user_id, new_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()

        # Step 1: Perform UPDATE
        cursor.execute('UPDATE users SET age = ? WHERE id = ?', (new_age, user_id))
        conn.commit()

        # Step 2: Fetch the updated user
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()

    return user

# Example Use
result = update_user_age_and_get(1, 36)
print("Updated User:", result)
```

---

### Function Example — Delete and Confirm Deletion

```python
def delete_user_and_confirm(user_id):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()

        # Step 1: Delete the user
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()

        # Step 2: Check if user still exists
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()

    return "Deleted Successfully" if user is None else "Deletion Failed"

# Example Use
print(delete_user_and_confirm(4))
```

---

### Function Example — Insert New User with Transaction Confirmation

```python
def insert_user_and_return_id(name, age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
        return cursor.lastrowid

# Example Use
new_id = insert_user_and_return_id("Grace", 31)
print(f"New user inserted with ID: {new_id}")
```

---

### Bonus Example — Fetch Updated Data into Pandas DataFrame

```python
import pandas as pd

def get_all_users_dataframe():
    with sqlite3.connect('lesson16.db') as conn:
        df = pd.read_sql_query('SELECT * FROM users', conn)
    return df

# Example Use
print(get_all_users_dataframe())
```

---

## **Homework Assignment: Build a Complete Python Mini-App**

### **Objective:**

Build a **Python application** that:

* Connects to an SQLite database
* Manages **customers** and **orders** using SQL operations
* Presents data with **Pandas**

---

###  **Required Features**

| Feature              | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| Database Connection  | Use `sqlite3` to connect to a local DB                              |
| Table Creation       | Create at least two related tables (e.g., `customers` and `orders`) |
| SQL Operations       | Perform `INSERT`, `SELECT`, `UPDATE`, and `DELETE`                  |
| JOIN                 | Implement at least one `INNER JOIN` between tables                  |
| Transactional Update | Perform an `UPDATE` and fetch the affected rows                     |
| Pandas Integration   | Fetch data with `pandas.read_sql_query()` and display               |


###  **Added Challenges (Optional)**

* Use `ORDER BY` or `GROUP BY` with Pandas
* Handle SQL errors with `try-except`
* Use functions for every major operation (CRUD pattern)

---


##  **Example Homework Structure Suggestion**

```
project_folder/
├── app.py                # Your main Python app with functions
├── requirements.txt      # Optional, list of libraries (e.g., pandas)
├── README.md             # Explain project, logic, SQL usage
├── lesson16.db           # Your SQLite database file (auto-created)
└── sample_output.png     # Optional, sample Pandas output screenshot
```

