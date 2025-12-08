# File handling in Python revolves around four main operations: open, read/write, close, and manage files.
# You use the open() function with different modes (r, w, a, rb, etc.),
# perform operations like read(), write(), or append(), and finally close the file with close().
# Real-time examples include reading configuration files, writing logs, or processing CSV data.
#1.Opening a File:
#=================
# syntax:
# file = open("filename.txt", "mode")
"""Modes:
r → Read (default)
w → Write (creates new file or overwrites existing)
a → Append (adds content at end)
rb / wb → Binary read/write"""
import csv
from pathlib import Path

ACCOUNTS_FILE = Path("accounts.csv")
TXN_FILE = Path("transactions.csv")

# Ensure files exist with headers
def init_files():
    if not ACCOUNTS_FILE.exists():
        with open(ACCOUNTS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["acc_no", "name", "balance"])
    if not TXN_FILE.exists():
        with open(TXN_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["acc_no", "type", "amount"])

def load_accounts():
    accounts = {}
    with open(ACCOUNTS_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            acc_no = int(row["acc_no"])
            accounts[acc_no] = {"name": row["name"], "balance": float(row["balance"])}
    return accounts

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["acc_no", "name", "balance"])
        for acc_no, data in accounts.items():
            writer.writerow([acc_no, data["name"], f'{data["balance"]:.2f}'])

def log_txn(acc_no, ttype, amount):
    with open(TXN_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([acc_no, ttype, f"{amount:.2f}"])

def create_account(acc_no, name, balance):
    accounts = load_accounts()
    if acc_no in accounts:
        print("Account already exists!")
        return
    if balance < 0:
        print("Initial balance cannot be negative.")
        return
    accounts[acc_no] = {"name": name, "balance": float(balance)}
    save_accounts(accounts)
    log_txn(acc_no, "Create", float(balance))
    print("Account created successfully!")

def deposit(acc_no, amount):
    if amount <= 0:
        print("Deposit amount must be positive.")
        return
    accounts = load_accounts()
    if acc_no not in accounts:
        print("Account not found!")
        return
    accounts[acc_no]["balance"] += float(amount)
    save_accounts(accounts)
    log_txn(acc_no, "Deposit", float(amount))
    print("Deposit recorded!")

def withdraw(acc_no, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return
    accounts = load_accounts()
    if acc_no not in accounts:
        print("Account not found!")
        return
    if accounts[acc_no]["balance"] < amount:
        print("Insufficient funds.")
        return
    accounts[acc_no]["balance"] -= float(amount)
    save_accounts(accounts)
    log_txn(acc_no, "Withdraw", float(amount))
    print("Withdrawal recorded!")

def check_balance(acc_no):
    accounts = load_accounts()
    if acc_no in accounts:
        data = accounts[acc_no]
        print(f"Balance for {data['name']}: {data['balance']:.2f}")
    else:
        print("Account not found!")

def transaction_history(acc_no):
    if not TXN_FILE.exists():
        print("No transactions yet.")
        return
    with open(TXN_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        found = False
        for row in reader:
            if int(row["acc_no"]) == acc_no:
                print(f"{row['type']}: {row['amount']}")
                found = True
        if not found:
            print("No transactions for this account.")

# Demo run
if __name__ == "__main__":
    init_files()
    create_account(1001, name="Anil", balance=500)
    deposit(1001, amount=500)
    withdraw(1001, amount=500)
    check_balance(1001)
    transaction_history(1001)





