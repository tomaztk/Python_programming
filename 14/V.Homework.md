### **LESSON 14: INTRODUCTION TO SQL FOR PYTHON DEVELOPERS**
---
### **Homework**

**Task:**
Write a series of SQL queries that:

1. Retrieve all customer names who have placed more than one order.
2. Insert a new order for a given customer.
3. Update an order's date.
4. Delete an order by ID.

**Documentation Requirement:**
For each query, explain:

* What the query does
* Why it would be useful in a real application
* How it could be integrated with Python (e.g., `sqlite3`, `pandas.read_sql_query`)

**Bonus:**
Export a SQL query result to a `.csv` using Python, e.g.:

```python
import pandas as pd
df = pd.read_sql_query("SELECT * FROM Orders", conn)
df.to_csv('orders.csv', index=False)
```

