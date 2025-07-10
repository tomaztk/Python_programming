
## **IV. Hands-on Exercise: Advanced SQL Techniques & Index Optimization**

---

### ** Goal:**

Apply **advanced SQL features**—including **subqueries**, **correlated subqueries**, **joins**, **advanced predicates**, and **index creation**—to solve business-relevant problems using the shared sample dataset.

---


### ** Dataset Summary (Reminder)**

You're working with the following tables:

* `users(user_id, name, email)`
* `orders(order_id, user_id, order_total, order_date)`
* `payments(payment_id, order_id, payment_date, amount)`
* `products(product_id, product_name, price, category)`

Sample data is described as SQL in earlier part of this lesson.

---

### ** Tasks & Queries**

---

####  **Task 1: Identify High-Spending Users Using a Subquery**

**Query:**

```sql
SELECT user_id, name
FROM users
WHERE user_id IN (
    SELECT user_id
    FROM orders
    GROUP BY user_id
    HAVING SUM(order_total) > (
        SELECT AVG(total_sum)
        FROM (
            SELECT user_id, SUM(order_total) AS total_sum
            FROM orders
            GROUP BY user_id
        ) AS user_totals
    )
);
```

**Explanation:**
Finds users whose total spending exceeds the **average total spending per user**.

---

####  **Task 2: Correlated Subquery – Most Recent Order per User**

**Query:**

```sql
SELECT u.name, o.order_id, o.order_date
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE o.order_date = (
    SELECT MAX(o2.order_date)
    FROM orders o2
    WHERE o2.user_id = u.user_id
);
```

**Explanation:**
Returns each user’s **latest order** using a correlated subquery.

---

#### **Task 3: Create an Index to Optimize Task 2**

**Query:**

```sql
CREATE INDEX idx_user_order_date ON orders(user_id, order_date);
```

**Explanation:**
This **composite index** speeds up filtering and sorting by `user_id` and `order_date`, which Task 2 depends on.

---

#### **Task 4: Use `ALL` Predicate – Premium Products**

**Query:**

```sql
SELECT product_name, price
FROM products
WHERE price > ALL (
    SELECT price FROM products WHERE category = 'Discount'
);
```

**Explanation:**
Returns all products priced higher than **every product** in the 'Discount' category.

---

#### **Task 5: Use `EXISTS` – Users with Orders Over \$100**

**Query:**

```sql
SELECT name
FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.user_id = u.user_id AND o.order_total > 100
);
```

**Explanation:**
Returns users who have made **at least one high-value purchase** over \$100.

---

#### **Task 6: Create a Partial Index to Optimize Task 5 (This part is optional)**

**Query:**

```sql
CREATE INDEX idx_high_order_total
ON orders(order_total)
WHERE order_total > 100;
```

**Explanation:**
This **partial index** is efficient for queries that filter orders **only when `order_total > 100`**.

---

#### **Task 7: Rewrite a Subquery Using JOIN – Users Who Made Payments**

**Original Query (subquery style):**

```sql
SELECT name
FROM users
WHERE user_id IN (
    SELECT o.user_id
    FROM orders o
    JOIN payments p ON o.order_id = p.order_id
);
```

**Rewritten with JOIN:**

```sql
SELECT DISTINCT u.name
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN payments p ON o.order_id = p.order_id;
```

**Explanation:**
Retrieves the same result using **explicit joins**; `DISTINCT` avoids duplicate names for users with multiple payments.

---

### Deliverables

For each task:

* Provide the SQL query (see above)
* Execute and verify the results
* Add a **brief explanation or comment** describing:

  * What the query does
  * Why the technique (subquery, join, index) is effective

