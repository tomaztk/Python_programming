import sqlite3
from logger import Logger

class dbManager:
    def __init__(self, db_path = "data/atm.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        
    def get_account_by_client(self, client_id):
        cur = self.conn.execute("SELECT account_id, client_id, balance  FROM Accounts WHERE client_id=?", (client_id,))
        s = Logger()
        s.log_action(account_id=1, action="GET_BALANCE_ACCOUNT", details="This")
        return cur.fetchone()