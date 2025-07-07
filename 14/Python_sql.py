import pandas as pd
import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to", db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def execute_query(conn, query):
    """Execute a single query."""
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print("Error executing query:", e)


def fetch_data(conn, query):
    """Fetch data from the database."""
    try:
        df = pd.read_sql_query(query, conn)
        print("Data fetched successfully")
        return df
    except sqlite3.Error as e:
        print("Error fetching data:", e)
        return None
    

def all_stuff():
    database = "example.db"

    # Create a database connection
    conn = create_connection(database)

    if conn is not None:
        # Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        );
        """
        execute_query(conn, create_table_query)

        # Insert data into the table
        insert_data_query = """
        INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25);
        """
        execute_query(conn, insert_data_query)

        # Fetch data from the table
        select_query = "SELECT * FROM users;"
        df = fetch_data(conn, select_query)
        print(df)

        # Close the connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")



database = "sample.db"
conn = create_connection(database)
select_query = "SELECT * FROM customers"
df = fetch_data(conn, select_query)
print(df)
