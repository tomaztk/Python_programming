
### Section 2

# Part 1
'''
import sqlite3
conn = sqlite3.connect('lesson16.db')
print("Database 'lesson16.db' created or opened successfully.")
conn.close()
'''

# Part 2
"""
import sqlite3
conn = sqlite3.connect('lesson16.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

conn.commit()
conn.close()

print("Table 'users' created successfully.")
"""

# Part 3
'''
import sqlite3

def create_user(name, age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
    print(f"User '{name}' added successfully.")


# Example Usage
create_user("Alice", 30)
create_user("Bob", 25)
'''


# Part 4
"""
import sqlite3
def fetch_all_users():
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
    return users

print(fetch_all_users())
"""

# Part 5
"""
import sqlite3

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

# Check for error
# insert_user_safe("Tom", -45i)

"""


# Part 6


"""
import sqlite3

def get_users_above_age(min_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE age > ?', (min_age,))
        users = cursor.fetchall()
    return users

# Example
print("Users older than 300:", get_users_above_age(300))

"""


# Part 7

import sqlite3

def update_user_age(name, new_age):
    with sqlite3.connect('lesson16.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
        conn.commit()
    print(f"Updated '{name}' to age {new_age}.")

# Example
update_user_age("Tom", 290)
