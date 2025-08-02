from db_manager import dbManager
#from logger import Logger

if __name__ == "__main__":
    db = dbManager()
    #logger = Logger()

    s = db.get_account_by_client(1)
    #logger.log_action(account_id=1, action="CHECK_BALANCE", details="Balance")
    print(s[2])