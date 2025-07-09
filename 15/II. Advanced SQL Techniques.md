
## **II. Advanced SQL Techniques**

---

### a. **Complex Queries with Subqueries and Advanced Predicates**

---

####  **Setup: Tables & Data**

```sql
-- USERS table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
);

-- ORDERS table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    order_total DECIMAL(10, 2),
    order_date DATE
);

-- PRODUCTS table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    category VARCHAR(50)
);
```

```sql
-- Sample USERS
INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com');

-- Sample ORDERS
INSERT INTO orders (user_id, order_total, order_date) VALUES
(1, 120.50, '2023-11-01'),
(1, 75.00, '2023-11-10'),
(2, 50.00, '2023-11-05'),
(3, 200.00, '2023-11-15');

-- Sample PRODUCTS
INSERT INTO products (product_name, price, category) VALUES
('Keyboard', 25.00, 'Accessories'),
('Monitor', 150.00, 'Electronics'),
('Mouse', 20.00, 'Accessories'),
('Budget Monitor', 90.00, 'Discount'),
('High-End Monitor', 250.00, 'Electronics');
```

---

#### **Example 1: Subquery to Find High-Spending Users**

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

**What it does:**
Returns users whose total spending is above the average order value across all users.

**Python Use Case:** Analytics module in a web app to identify "VIP customers".

```python
cursor.execute("""
    SELECT user_id, name
    FROM users
    WHERE user_id IN (
        SELECT user_id
        FROM orders
        GROUP BY user_id
        HAVING SUM(order_total) > (
            SELECT AVG(order_total) FROM orders
        )
    )
""")
vip_users = cursor.fetchall()
```

---

#### **Example 2: Using `ALL` Predicate**

```sql
SELECT product_name FROM products
WHERE price > ALL (
    SELECT price FROM products WHERE category = 'Discount'
);
```

**What it does:**
Finds products priced higher than **all** products in the 'Discount' category.

**Python Use Case:** Recommendation system to promote premium products.

```python
cursor.execute("""
    SELECT product_name FROM products
    WHERE price > ALL (
        SELECT price FROM products WHERE category = 'Discount'
    )
""")
premium_products = cursor.fetchall()
```

---

#### **Example 3: `EXISTS` Predicate**

```sql
SELECT name
FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.user_id AND o.order_total > 100
);
```

**What it does:**
Returns users who have placed **at least one order** over \$100.

**Why `EXISTS` is efficient:**
Stops scanning as soon as one matching record is found.

**Python Use Case:** Conditional content delivery (e.g., “Thanks for your big purchase!”).

---

###  **Example 4: Correlated Subquery — Latest Order per User**

```sql
SELECT u.name, o.order_id, o.order_date
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE o.order_date = (
    SELECT MAX(order_date)
    FROM orders o2
    WHERE o2.user_id = u.user_id
);
```

**What it does:**
For each user, returns only their **most recent order**.

**Python Use Case:**
Generating personalized dashboards that show the most recent activity per user.

---

### **Example 5: Subquery in SELECT Clause — Total Spend per User**

```sql
SELECT u.name,
       (SELECT SUM(order_total)
        FROM orders o
        WHERE o.user_id = u.user_id) AS total_spent
FROM users u;
```

**What it does:**
Displays each user along with the **sum of their orders**, using a subquery in the `SELECT` clause.

**Python Use Case:**
Used in email personalization (“Hi Alice, you’ve spent \$XXX this month!”)

---

### **Example 6: NOT EXISTS — Users With No Orders**

```sql
SELECT name
FROM users u
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.user_id = u.user_id
);
```

**What it does:**
Lists all users who have **never placed an order**.

**Python Use Case:**
Useful for retention campaigns or reactivation emails.

---

### **Example 7: `IN` with Aggregate Filtering — Users with More Than One Order**

```sql
SELECT name
FROM users
WHERE user_id IN (
    SELECT user_id
    FROM orders
    GROUP BY user_id
    HAVING COUNT(order_id) > 1
);
```

**What it does:**
Returns users who have placed **more than one** order.

**Python Use Case:**
Rewarding returning customers or tracking engagement.

---

### **Example 8: ALL with Correlated Comparison — Expensive Products Only**

```sql
SELECT product_name
FROM products
WHERE price > ALL (
    SELECT price FROM products WHERE category = 'Accessories'
);
```

**What it does:**
Selects products more expensive than **every** item in the 'Accessories' category.

**Python Use Case:**
Used for upselling strategies in e-commerce apps.

---

### **Example 9: Nested Subqueries — Top Spender**

```sql
SELECT name
FROM users
WHERE user_id = (
    SELECT user_id
    FROM orders
    GROUP BY user_id
    ORDER BY SUM(order_total) DESC
    LIMIT 1
);
```

**What it does:**
Returns the user who has spent the **most overall**.

**Python Use Case:**
For leaderboard displays, loyalty programs, or admin analytics.

---

### **Example 10: EXISTS with JOIN — Users Who Paid Exactly What They Ordered**

```sql
SELECT u.name
FROM users u
WHERE EXISTS (
    SELECT 1
    FROM orders o
    JOIN payments p ON o.order_id = p.order_id
    WHERE o.user_id = u.user_id AND o.order_total = p.amount
);
```

**What it does:**
Finds users whose **orders were fully paid** (no discounts, no outstanding balances).

**Python Use Case:**
Reconciliation logic or identifying complete transactions for reporting.

---

### 📌 **Example 11: Subquery in `FROM` Clause — Average Spend per User**

```sql
SELECT name, avg_spent
FROM (
    SELECT u.user_id, u.name, AVG(o.order_total) AS avg_spent
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    GROUP BY u.user_id
) AS user_avg;
```

**What it does:**
Calculates and displays average order value **per user**.

**Python Use Case:**
Behavioral segmentation based on spending patterns.


### b. **Enhanced SQL Joins for Multi-Table Queries**

---

#### **Add PAYMENTS Table & Data**

```sql
-- PAYMENTS table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    payment_date DATE,
    amount DECIMAL(10, 2)
);

-- Sample PAYMENTS
INSERT INTO payments (order_id, payment_date, amount) VALUES
(1, '2023-11-02', 120.50),
(2, '2023-11-11', 75.00),
(3, '2023-11-06', 50.00),
(4, '2023-11-16', 200.00);
```

---

#### **Example 4: Join for Full Transaction History**

```sql
SELECT u.name, o.order_id, o.order_total, p.payment_date, p.amount
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN payments p ON o.order_id = p.order_id;
```

**What it does:**
Combines user names, their orders, and payment details in one view.

**Python Use Case:**
Data export tool or dashboard backend showing detailed purchase logs.

```python
cursor.execute("""
    SELECT u.name, o.order_id, o.order_total, p.payment_date, p.amount
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    JOIN payments p ON o.order_id = p.order_id
""")
transactions = cursor.fetchall()
```

---

#### **Example 5: LEFT JOIN to Show Users With or Without Orders**

```sql
SELECT u.name, o.order_id
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id;
```

**What it does:**
Returns all users, with their orders if any — includes users who haven’t ordered yet.

**Python Use Case:**
Generating reports for user engagement (e.g., for marketing or email campaigns).

---

#### **Example 6: Aggregated Joins**

```sql
SELECT u.name, COUNT(o.order_id) AS total_orders, SUM(o.order_total) AS total_spent
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id;
```

**What it does:**
Shows number of orders and total spend per user.

**Python Use Case:**
Dashboard summary for business stakeholders or automated email personalization.

