import pandas as pd
import matplotlib.pyplot as plt
import os

class DataAnalyzer:
    def __init__(self, db_manager):
        self.db = db_manager
        os.makedirs("plots", exist_ok=True)

    def _load_transactions_df(self, account_id):
        rows = self.db.get_transactions(account_id)
        df = pd.DataFrame(rows, columns=["id", "account_id", "merchant", "amount", "type", "datetime"])
        df["datetime"] = pd.to_datetime(df["datetime"])
        return df

    def plot_balance_over_time(self, account_id):
        df = self._load_transactions_df(account_id)
        df["balance"] = df["amount"].cumsum()
        plt.figure()
        plt.plot(df["datetime"], df["balance"], marker="o")
        plt.title("Balance Over Time")
        plt.savefig("plots/balance_over_time.png")

    def plot_payments_by_merchant(self, account_id):
        df = self._load_transactions_df(account_id)
        merchant_totals = df.groupby("merchant")["amount"].sum()
        plt.figure()
        merchant_totals.plot(kind="bar")
        plt.title("Payments by Merchant")
        plt.savefig("plots/payments_by_merchant.png")

    def print_statistics(self, account_id):
        df = self._load_transactions_df(account_id)
        print("Mean:", df["amount"].mean())
        print("Min:", df["amount"].min())
        print("Max:", df["amount"].max())
        print("Median:", df["amount"].median())
        print("Std Dev:", df["amount"].std())
