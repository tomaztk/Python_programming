# **IV. Advanced Queries and Integration with Functions & Pandas**

---

## Topics Covered:

* Using SQL **JOINS** to link data across tables
* Embedding SQL logic in **reusable Python functions**
* Reading SQL results into **Pandas DataFrames**
* Using Pandas for simple data exploration

---

## **Key Concept**

A relational database often contains **multiple related tables**.
**JOIN operations** allow you to retrieve combined data based on relationships (e.g., users with their orders).
Pandas is a powerful library that can turn query results into DataFrames for further analysis.

---

## **1. Setting Up Related Tables**

### Users Table — (already created in earlier sections)

### Creating a Related `orders` Table

```python
def create_orders_table():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')
        conn.commit()
    print("Orders table created or confirmed existing.")

# Run once to ensure table exists
create_orders_table()
```

---

## **2. Insert Sample Data for JOIN Demonstration**

```python
def add_order(user_id, product):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders (user_id, product) VALUES (?, ?)', (user_id, product))
        conn.commit()
    print(f"Order '{product}' added for user ID {user_id}.")

# Example Usage
add_user("Charlie", 32)
add_user("Dana", 29)

add_order(3, "Smartphone")  # Assuming Charlie is ID 3
add_order(4, "Tablet")      # Assuming Dana is ID 4
```

---

## **3. Performing INNER JOIN with Python & SQLite**

###  Inner Join Function to Fetch Combined Data

```python
def fetch_users_with_orders():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT users.name, users.age, orders.product
        FROM users
        INNER JOIN orders ON users.id = orders.user_id
        ''')
        results = cursor.fetchall()
    return results

# Example Output
print("Users with their Orders:")
for row in fetch_users_with_orders():
    print(row)
```

### What Does INNER JOIN Do?

* Combines **users** and **orders** based on `user_id`
* Only returns rows where the user has at least one order
* Allows pulling relational data in a single query

---

## **4. Integrating with Pandas for Data Analysis**

```python
import pandas as pd

def get_users_orders_dataframe():
    with sqlite3.connect('lesson16.db') as conn:
        df = pd.read_sql_query('''
        SELECT users.id, users.name, users.age, orders.product
        FROM users
        INNER JOIN orders ON users.id = orders.user_id
        ''', conn)
    return df

# Example
df_users_orders = get_users_orders_dataframe()
print("\nUsers and their Orders DataFrame:")
print(df_users_orders)
```

---

## **5. (optional): Use Pandas to Explore Data**

```python
# Count orders per user
order_counts = df_users_orders.groupby('name').size().reset_index(name='Order Count')
print("\nOrder Count per User:")
print(order_counts)

# Filter users older than 30 with their orders
older_users_orders = df_users_orders[df_users_orders['age'] > 30]
print("\nUsers older than 30 with their Orders:")
print(older_users_orders)
```

---

## **Concepts**

| Concept                | How It's Done                                   |
| ---------------------- | ----------------------------------------------- |
| Create Related Tables  | Define tables with `FOREIGN KEY` constraints    |
| Insert Related Data    | Insert into both parent and child tables        |
| INNER JOIN             | Combine rows across tables with matching keys   |
| Embed SQL in Functions | Wrap SQL logic inside Python functions          |
| Use Pandas             | Import query results as DataFrames for analysis |

---

## **Recap**

* SQL JOINs allow you to pull related data across multiple tables.
* Embedding SQL queries in Python functions makes your code modular and reusable.
* Using Pandas with SQL result sets turns your data into powerful, easy-to-analyze tables.
* Pandas supports filtering, grouping, and summarizing SQL data within Python.

-
