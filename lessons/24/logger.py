import csv
import datetime
import os

class Logger:
    def __init__(self, log_file="logs/actions.csv", error_file="logs/errors.txt"):
        self.log_file = log_file
        self.error_file = error_file

        # Creates dir / files is not exists!!!
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        if not os.path.exists(log_file):
            with open(log_file, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["datetime", "account_id", "action", "details"])


    def log_action(self, account_id, action, details=""):
        """Log user actions to CSV file."""
        try:
            with open(self.log_file, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    account_id,
                    action,
                    details
                ])
        except Exception as e:
            self.log_error(f"Failed to log action: {e}")

    def log_error(self, error_message):
        """Log errors to TXT file."""
        try:
            with open(self.error_file, mode="a", encoding="utf-8") as f:
                f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {error_message}\n")
        except Exception as e:
            print(f"Error logging failed: {e}")

    def read_errors(self):
        """Read all logged errors."""
        if os.path.exists(self.error_file):
            with open(self.error_file, "r", encoding="utf-8") as f:
                return f.read()
        return "No errors logged."
