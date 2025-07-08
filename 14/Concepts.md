
## Concepts
### **1. What is an RDBMS?**

**RDBMS** stands for **Relational Database Management System**. It is a software system used to manage relational databases — databases that store data in **tables** (also called relations).

* Each table consists of **rows** (records) and **columns** (attributes or fields).
* Data in RDBMS is organized to reduce redundancy and ensure data integrity.

Popular RDBMSs include **MySQL**, **PostgreSQL**, **Oracle**, **SQL Server**, and **SQLite**.

---

### **2. Why Do We Use Tables in RDBMS?**

Tables:

* Represent **entities** (like customers, orders, products, etc.).
* Are easy to visualize, manage, and query.
* Help in maintaining structured and related data.

Example:

```text
Customers Table:
+----+----------+-----------+
| ID | Name     | Email     |
+----+----------+-----------+
| 1  | Alice    | a@x.com   |
| 2  | Bob      | b@x.com   |
+----+----------+-----------+
```

---

### **3. What is Normalization? What are Normal Forms?**

**Normalization** is the process of organizing data to reduce redundancy and improve data integrity.

It involves splitting data into multiple tables and defining relationships between them.

#### Common Normal Forms:

1. **1NF (First Normal Form)**:

   * No repeating groups or arrays.
   * Each field contains only atomic (indivisible) values.

2. **2NF (Second Normal Form)**:

   * Must be in 1NF.
   * No partial dependency (every non-key column depends on the whole primary key).

3. **3NF (Third Normal Form)**:

   * Must be in 2NF.
   * No transitive dependencies (non-key column depends only on the primary key).

Higher forms (like BCNF, 4NF) are more advanced and used in specific scenarios.

---

### **4. What is a Primary Key?**

A **Primary Key** is a column (or set of columns) that uniquely identifies each row in a table.

* Cannot be NULL.
* Must be unique.

Example:

```text
Customer(ID int PRIMARY KEY, Name varchar)
```

---

### **5. What is a Foreign Key?**

A **Foreign Key** is a column (or set of columns) in one table that refers to the **Primary Key** in another table.

* It establishes a **relationship** between two tables.
* Maintains **referential integrity**.

Example:

```text
Orders Table:
+----+------------+-------------+
| ID | CustomerID | OrderTotal  |
+----+------------+-------------+
| 1  | 1          | 100.00      |
| 2  | 2          | 150.00      |
+----+------------+-------------+
```

Here, `CustomerID` is a foreign key referring to `Customers(ID)`.

---

### **6. What is Data Integrity?**

**Data Integrity** ensures that the data in the database is accurate and consistent.

Types:

* **Entity Integrity**: Ensures each table has a primary key and unique rows.
* **Referential Integrity**: Ensures that foreign keys correctly reference primary keys in other tables.
* **Domain Integrity**: Ensures that data entries are valid for the column's data type and constraints (like NOT NULL, CHECK, etc.).

---

### **7. Why Use Relationships Between Tables?**

Relationships allow you to:

* Avoid data duplication (e.g., no need to repeat customer info in every order).
* Maintain consistency (e.g., if a customer is deleted, you know what to do with related orders).
* Query related data easily using **JOINs**.

