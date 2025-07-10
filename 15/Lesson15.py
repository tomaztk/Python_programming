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


con = sqlite3.connect("lesson15.db")
cur = con.cursor()
res = cur.execute(query)
df = res.fetchall()
con.close()

pd_df = pd.DataFrame(df, columns=['Name', 'OrderID', 'OrderDate'])
print(pd_df)