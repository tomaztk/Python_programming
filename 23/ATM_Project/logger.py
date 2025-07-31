import csv
import os
from datetime import datetime

class Logger:
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        self.action_log = "logs/actions_log.csv"
        self.error_log = "logs/error_log.txt"

    def log_action(self, client_id, action, details=""):
        with open(self.action_log, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), client_id, action, details])

    def log_error(self, error_message):
        with open(self.error_log, "a") as f:
            f.write(f"{datetime.now()} - ERROR: {error_message}\n")
