## **LESSON 15: ADVANCED SQL CONCEPTS WITH PYTHON APPLICATIONS**


#### **1. Recap of Previous Lesson**

* Review of intermediate SQL concepts and basic Python-SQL integration.
* Overview of database drivers (e.g., `sqlite3`, `psycopg2`, `SQLAlchemy`).

---

#### **2. Advanced SQL Techniques**

##### a. **Complex Queries with Subqueries and Advanced Predicates**

* **Subqueries**:

  * Example: Fetch users who placed orders greater than the average order value.

    ```sql
    SELECT user_id, name
    FROM users
    WHERE user_id IN (
        SELECT user_id
        FROM orders
        GROUP BY user_id
        HAVING SUM(order_total) > (
            SELECT AVG(order_total) FROM orders
        )
    );
    ```

    **Python Context:** Use subqueries within Python functions that require filtering based on aggregate data.

* **Advanced Predicates** (`IN`, `EXISTS`, `ANY`, `ALL`):

  * Example:

    ```sql
    SELECT product_name FROM products
    WHERE price > ALL (
        SELECT price FROM products WHERE category = 'Discount'
    );
    ```

    **Explanation:** Useful for comparative filtering in analytics modules.

---

##### b. **Enhanced SQL Joins for Multi-Table Queries**

* **Types of Joins**: `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`, `CROSS`
* **Use Case in Python**:

  * Joining `users`, `orders`, and `payments` for a full transaction history:

    ```sql
    SELECT u.name, o.order_id, p.payment_date, p.amount
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    JOIN payments p ON o.order_id = p.order_id;
    ```

    **Python Example**:

    ```python
    cursor.execute("""SELECT u.name, o.order_id, p.payment_date, p.amount
                      FROM users u
                      JOIN orders o ON u.user_id = o.user_id
                      JOIN payments p ON o.order_id = p.order_id""")
    results = cursor.fetchall()
    ```

---

#### **3. Query Optimization for Python Applications**

##### a. **Indexing and Performance**

* Use `EXPLAIN` or `EXPLAIN ANALYZE` to understand query execution plans.
* Add indexes on frequently queried columns.

  ```sql
  CREATE INDEX idx_user_id ON orders(user_id);
  ```

  **Python Benefit:** Reduces API latency in data-heavy endpoints.

##### b. **Limiting Result Sets**

* Avoid loading large datasets into memory:

  ```sql
  SELECT * FROM logs LIMIT 100 OFFSET 0;
  ```

  **Python Tip:** Use generators or pagination when working with large queries.

##### c. **Prepared Statements and Parameterization**

* Prevents SQL injection and speeds up repeated queries.

  ```python
  cursor.execute("SELECT * FROM users WHERE email = %s", (user_email,))
  ```

##### d. **Connection Pooling (e.g., with SQLAlchemy or `psycopg2.pool`)**

* Reuses DB connections across requests in web apps.

  ```python
  from psycopg2 import pool
  connection_pool = pool.SimpleConnectionPool(1, 10, user="postgres", ...)
  ```

---

#### **4. Hands-on Exercise**

* **Goal:** Optimize a provided set of SQL queries.
* **Tasks:**

  1. Identify bottlenecks using `EXPLAIN`.
  2. Add indexes where necessary.
  3. Rewrite queries to use joins instead of subqueries (where optimal).
  4. Refactor Python code to batch-fetch and paginate large result sets.

---

### **New Additional Topics**

#### **5. SQLAlchemy ORM vs Raw SQL for Optimization**

* **Example with SQLAlchemy Query Optimization**:

  ```python
  session.query(User).filter(User.orders.any(Order.total > 100)).all()
  ```

  * Compare with raw SQL for performance in profiling.

#### **6. Using Materialized Views and Caching with Python**

* **Materialized View**:

  ```sql
  CREATE MATERIALIZED VIEW top_customers AS
  SELECT user_id, SUM(order_total) AS total
  FROM orders
  GROUP BY user_id
  ORDER BY total DESC;
  ```

  * Refreshing the view in Python:

    ```python
    cursor.execute("REFRESH MATERIALIZED VIEW top_customers")
    ```

#### **7. Python Profiling Tools for SQL Performance**

* Using `sqlalchemy.echo`, `time`, or `cProfile` to measure query performance.
* Integration with APM tools (e.g., Datadog, New Relic).

---

### **Homework**

**Assignment:**

* Optimize a set of 3 SQL queries used in a mock Python web application (provided).
* Include:

  * Before-and-after versions.
  * EXPLAIN output summary.
  * Python-side improvements (e.g., batching, caching).
  * A short write-up on performance gains.

