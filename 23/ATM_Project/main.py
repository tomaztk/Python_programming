from db_manager import DatabaseManager
from logger import Logger
from data_analyzer import DataAnalyzer
from atm import ATM

if __name__ == "__main__":
    db = DatabaseManager()
    logger = Logger()
    analyzer = DataAnalyzer(db)
    atm = ATM(db, logger, analyzer)

    # Optional: Add a test client
    if not db.get_client_by_pin("1234"):
        client_id = db.add_client("John Doe", "1234", "john@example.com")
        db.add_account(client_id, 500.0, "debit")

    client, account = atm.login()
    if client:
        atm.main_menu(client, account)
