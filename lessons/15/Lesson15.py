import sqlite3
import pandas as pd 

query = """
SELECT u.name, o.order_id, o.order_date
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE o.order_date = (
    SELECT MAX(order_date)
    FROM orders o2
    WHERE o2.user_id = u.user_id
);
"""


query2 = """
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
"""


con = sqlite3.connect("lesson15_v1.db")
cur = con.cursor()
res = cur.execute(query2)
df = res.fetchall()
con.close()

pd_df = pd.DataFrame(df, columns=['UserID', 'Name'])
print(pd_df)