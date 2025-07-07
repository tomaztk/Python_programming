import sqlite3

# con = sqlite3.connect("/Users/tomazkastrun/Documents/tomaztk_github/Python_programming/14/sample.db")
con = sqlite3.connect("sample.db")
cur = con.cursor()
#res = cur.execute("SELECT * FROM Customers")
#res.fetchone()
#CustomerID, Name, Email = res.fetchone()
#print(f'The Customer is {CustomerID!r}, with name {Name} and email {Email}')
#con.close()


for row in cur.execute("SELECT * FROM Customers"):
    print(row)
con.close()