class ATM:
    def __init__(self, db_manager, logger, data_analyzer):
        self.db = db_manager
        self.logger = logger
        self.analyzer = data_analyzer

    def login(self):
        for _ in range(3):
            pin = input("Enter your 4-digit PIN: ")
            if not (pin.isdigit() and len(pin) == 4):
                print("Invalid PIN format!")
                continue
            client = self.db.get_client_by_pin(pin)
            if client:
                print(f"Welcome {client[1]}!")
                account = self.db.get_account_by_client(client[0])
                return client, account
            else:
                print("PIN not found.")
        print("Too many failed attempts.")
        return None, None

    def main_menu(self, client, account):
        while True:
            print("\n--- MY PERSONAL ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit Money (Income)")
            print("3. Withdraw Money")
            print("4. Make Payment")
            print("5. View Statistics")
            print("6. Exit")

            choice = input("Select option: ")
            if choice == "1":
                self.check_balance(account)
            elif choice == "2":
                self.deposit_money(account)
            elif choice == "3":
                self.withdraw_money(account)
            elif choice == "4":
                self.make_payment(account)
            elif choice == "5":
                self.view_statistics(account)
            elif choice == "6":
                break
            else:
                print("Invalid choice!")

    def check_balance(self, account):
        print(f"Your balance is: {account[2]:.2f}")
        self.logger.log_action(account[1], "CHECK_BALANCE")


    def deposit_money(self, account):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Deposit must be positive.")
            new_balance = account[2] + amount
            self.db.update_balance(account[0], new_balance)
            self.db.add_transaction(account[0], "Deposit", amount, "deposit")
            self.logger.log_action(account[1], "DEPOSIT", amount)
            print("Deposit successfully added.")
            account = self.db.get_account_by_client(account[1])
            
            new_amount = self.db.get_account_by_client(account[1])
            print("Your new balacne is:", new_amount[2])

        except Exception as e:
            self.logger.log_error(str(e))
            print("Error during deposit.")

    def withdraw_money(self, account):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0 or amount > account[2]:
                raise ValueError("Invalid withdrawal amount.")
            new_balance = account[2] - amount
            self.db.update_balance(account[0], new_balance)
            self.db.add_transaction(account[0], "ATM Withdrawal", -amount, "withdrawal")
            self.logger.log_action(account[1], "WITHDRAW", amount)
            print("Withdrawal successful.")
            account = self.db.get_account_by_client(account[1])
        except Exception as e:
            self.logger.log_error(str(e))
            print("Error during withdrawal.")

    def make_payment(self, account):
        try:
            merchant = input("Enter merchant name: ")
            amount = float(input("Enter amount: "))
            if amount <= 0 or amount > account[2]:
                raise ValueError("Invalid payment amount.")
            new_balance = account[2] - amount
            self.db.update_balance(account[0], new_balance)
            self.db.add_transaction(account[0], merchant, -amount, "payment")
            self.logger.log_action(account[1], "PAYMENT", f"{merchant}:{amount}")
            print("Payment successful.")
            account = self.db.get_account_by_client(account[1])
        except Exception as e:
            self.logger.log_error(str(e))
            print("Error during payment.")

    def view_statistics(self, account):
        self.analyzer.print_statistics(account[0])
        self.analyzer.plot_balance_over_time(account[0])
        self.analyzer.plot_payments_by_merchant(account[0])
        print("Statistics & plots generated.")