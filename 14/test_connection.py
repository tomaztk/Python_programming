import sqlite3

# one way :)
'''
con = sqlite3.connect("shop.db")
cur = con.cursor()

query = 
SELECT
    Customers.Name AS Customer,
    Products.Name AS Product,
    Orders.Quantity,
    Orders.OrderDate
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
JOIN Products ON Orders.ProductID = Products.ProductID;


for row in cur.execute(query):
    print(row)
con.close()
'''


# or another way :)

# con = sqlite3.connect("/Users/tomazkastrun/Documents/tomaztk_github/Python_programming/14/sample.db")
con = sqlite3.connect("shop.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM Customers")
df = res.fetchall()
#CustomerID, Name, Email = res.fetchone()
#print(f'The Customer is {CustomerID!r}, with name {Name} and email {Email}')
con.close()


# print(df)
import pandas as pd 


pd_df = pd.DataFrame(df, columns=['CustomerID', 'Name', 'Email'])
print(pd_df)