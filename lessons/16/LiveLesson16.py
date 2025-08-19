import sqlite3
import pandas as pd


#conn = sqlite3.connect('lesson16.db')
#conn.close()

def create_user2_table():
    conn = sqlite3.connect('lesson16.db')
    cursor = conn.cursor()
    
    # Create 'users' table if it doesn't exist already
    cursor.execute('''
    CREATE TABLE users2 (
        id INTEGER NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Table created!")


def create_user(name, age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
    print(f"User '{name}' added successfully.")


# create_user2_table()

# create_user("Bojan", 31)
# create_user("Bob", 25)

select_stmt = """select 
        id,
         name,
          age from users"""

def get_all_users():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute(select_stmt)
        users = cursor.fetchall()
    return users





def add_user(name, age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
    print(f"User '{name}' added successfully.")

# Example
# add_user("David", 27)

# print(get_all_users())




def get_users_above_age(min_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT Name FROM users WHERE age > ?', (min_age,))
        users = cursor.fetchall()
    return users

# Example
# print("Users older than 31:", get_users_above_age(31))



def get_youngest_users(limit):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY age ASC LIMIT ?', (limit,))
        users = cursor.fetchall()
    return users

# Example
# print("Top 2 youngest users:", get_youngest_users(2))



def update_user_age(name, new_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
        conn.commit()
    print(f"Updated '{name}' to age {new_age}.")

# Example
# update_user_age("Bojan", 31)
# print(get_all_users())


def delete_user(name):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE name = ?', (name,))
        conn.commit()
    print(f"User '{name}' deleted.")

# Example
# delete_user("Bojan")
# print(get_all_users())


# UPDATE  --- WHERE!!!!
# DELETE  --- WHERE!!!!


def user_workflow_demo():
    add_user("Frank", 40)
    print("All users after adding Frank:", get_all_users())

    update_user_age("Frank", 41)
    print("All users after updating Frank:", get_all_users())

    ##delete_user("Frank")
    ## print("All users after deleting Frank:", get_all_users())



# user_workflow_demo()


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


# create_orders_table()


def add_order(user_id, product):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders (user_id, product) VALUES (?, ?)', (user_id, product))
        conn.commit()
    print(f"Order '{product}' added for user ID {user_id}.")

# Example Usage
# add_user("Charlie", 32)
# add_user("Dana", 29)

# print(get_all_users())

# add_order(12, "Smartphone")  # Assuming Charlie is ID 3
# add_order(13, "Tablet")      # Assuming Dana is ID 4




def get_all_orders():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
    return orders

# print(get_all_orders())




def fetch_users_with_orders():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT users.name, users.age, orders.product
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
        ''')
        results = cursor.fetchall()
    return results

# Example Output
#print("Users with their Orders:")
#for row in fetch_users_with_orders():
#    print(row)



import pandas as pd

def get_users_orders_dataframe():
    with sqlite3.connect('lesson16.db') as conn:
        df = pd.read_sql_query('''
        SELECT users.id, users.name, users.age, orders.product
        FROM users
        INNER JOIN orders ON users.id = orders.user_id
        WHERE users.age > 25
        ''', conn)
    return df

# Example
df_users_orders = get_users_orders_dataframe()


# Count orders per user
order_counts = df_users_orders.groupby('name').size().reset_index(name='Order Count')
print("\nOrder Count per User:")
print(order_counts)

# Filter users older than 30 with their orders
older_users_orders = df_users_orders[df_users_orders['age'] > 30]
print("\nUsers older than 30 with their Orders:")
print(older_users_orders)