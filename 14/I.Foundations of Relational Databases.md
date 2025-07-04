### **1. Foundations of Relational Databases**

---

Relational databases are a **foundational technology** in computer science used to store structured data. They organize information into **tables (also called relations)**, where:

* **Rows** represent **individual records**.
* **Columns** represent **attributes** of the data.
* **Primary keys** uniquely identify records in a table.
* **Foreign keys** establish relationships between tables.

This model enables you to **link data across tables**, reducing redundancy and improving consistency.

---

#### ** Historical Background:**

The **relational model** was proposed by **Edgar F. Codd** in **1970** in a landmark paper titled *"A Relational Model of Data for Large Shared Data Banks"*. Codd’s model provided a mathematical foundation using **set theory** and **predicate logic**, which made it easier to query and manipulate data using a **declarative language** (like SQL). (source: wiki stuff)

Key milestones:

* **1979**: First commercial RDBMS (Oracle v2)
* **1986**: SQL standardized by ANSI
* **1990s–2000s**: Dominance of relational systems like Oracle, MSSQL Server, MySQL, PostgreSQL
* **Today**: RDBMS still dominate, though often complemented by specialized systems (e.g., NoSQL, time-series DBs)

---

#### **Key Concepts in Relational Databases:**

| Concept                             | Description                                                 |
| ----------------------------------- | ----------------------------------------------------------- |
| **Table**                           | A collection of rows and columns. Also called a "relation". |
| **Row (Record)**                    | A single entry in a table.                                  |
| **Column (Field)**                  | A data attribute for the record.                            |
| **Primary Key**                     | A column (or set) that uniquely identifies a row.           |
| **Foreign Key**                     | A reference to the primary key in another table.            |
| **SQL (Structured Query Language)** | The language used to manage and query relational databases. |

---

#### **Popular Relational Database Systems (RDBMS Providers):**

| Provider       | Notable Product | Description                              |
| -------------- | --------------- | ---------------------------------------- |
| **Oracle**     | Oracle DB       | Enterprise-grade, widely used            |
| **Microsoft**  | SQL Server      | Windows-integrated, powerful GUI tools   |
| **IBM**        | Db2             | Strong in legacy enterprise environments |
| **PostgreSQL** | PostgreSQL      | Open-source, standards-compliant, robust |
| **MySQL**      | MySQL, MariaDB  | Widely used in web development           |
| **SQLite**     | SQLite          | Lightweight, file-based, embedded use    |

---

#### **Other Database Paradigms (Beyond Relational):**

| Type            | Examples              | Use Case                                        |
| --------------- | --------------------- | ----------------------------------------------- |
| **NoSQL**       | MongoDB, Couchbase    | Unstructured or semi-structured data            |
| **Time-Series** | InfluxDB, TimescaleDB | Sensor data, logs, time-stamped events          |
| **Key-Value**   | Redis, DynamoDB       | Fast lookup of values by key                    |
| **Document**    | MongoDB, CouchDB      | JSON/BSON structured documents                  |
| **Graph**       | Neo4j, ArangoDB       | Complex relationships (social networks, graphs) |

---

#### **Creating a Simple Relational Model in SQLite**

Let’s create a **SQLite database** with three connected tables: `Customers`, `Orders`, and `Products`.

```sql
%CREATE shop.db shopdb

-- Create Customers table
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL
);

-- Create Products table
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL
);

-- Create Orders table
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT NOT NULL,
    CustomerID INTEGER NOT NULL,
    ProductID INTEGER NOT NULL,
    Quantity INTEGER NOT NULL,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
);
```

---

#### **INSERT Statements:**

```sql
-- Insert Customers
INSERT INTO Customers (Name, Email) VALUES ('Alice Smith', 'alice@example.com');
INSERT INTO Customers (Name, Email) VALUES ('Bob Johnson', 'bob@example.com');

-- Insert Products
INSERT INTO Products (Name, Price) VALUES ('Laptop', 1200.00);
INSERT INTO Products (Name, Price) VALUES ('Headphones', 150.00);

-- Insert Orders
INSERT INTO Orders (OrderDate, CustomerID, ProductID, Quantity)
VALUES ('2025-07-01', 1, 1, 1);  -- Alice buys a Laptop

INSERT INTO Orders (OrderDate, CustomerID, ProductID, Quantity)
VALUES ('2025-07-02', 2, 2, 2);  -- Bob buys two Headphones
```

---

#### **Example Query: Join Customers and Orders**

```sql
SELECT
    Customers.Name AS Customer,
    Products.Name AS Product,
    Orders.Quantity,
    Orders.OrderDate
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
JOIN Products ON Orders.ProductID = Products.ProductID;
```

