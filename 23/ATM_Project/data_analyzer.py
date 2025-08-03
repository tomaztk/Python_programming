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

    def plot_balance_over_time_old(self, account_id):
        df = self._load_transactions_df(account_id)
        df["balance"] = df["amount"].cumsum()
        plt.figure()
        plt.plot(df["datetime"], df["balance"], marker="o")
        plt.title("Balance Over Time")
        plt.savefig("plots/balance_over_time.png")
        plt.close()


    def plot_balance_over_time(self, account_id):
        df = self._load_transactions_df(account_id)
        df["date"] = df["datetime"].dt.date
        daily_df = df.groupby("date", as_index=False)["amount"].sum()
        daily_df["balance"] = daily_df["amount"].cumsum()
        plt.figure(figsize=(10, 6))
        plt.plot(daily_df["date"], daily_df["balance"], marker="o", linestyle="-", linewidth=2)
        plt.title("Balance Over Time", fontsize=16)
        plt.xlabel("Date", fontsize=14)
        plt.ylabel("Balance", fontsize=14)
        plt.xticks(rotation=90)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.savefig("plots/balance_over_time.png", dpi=300)
        plt.close()


    def plot_payments_by_merchant(self, account_id):
        df = self._load_transactions_df(account_id)
        merchant_totals = df.groupby("merchant")["amount"].sum()
        plt.figure(figsize=(10, 6))
        merchant_totals.plot(kind="bar")
        plt.title("Payments by Merchant", fontsize=16)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.savefig("plots/payments_by_merchant.png", dpi=300)
        plt.close()

    def print_statistics(self, account_id):
        df = self._load_transactions_df(account_id)
        print("Mean:", df["amount"].mean())
        print("Min:", df["amount"].min())
        print("Max:", df["amount"].max())
        print("Median:", df["amount"].median())
        print("Std Dev:", df["amount"].std())
