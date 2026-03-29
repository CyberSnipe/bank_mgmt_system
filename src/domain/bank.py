import json
from .bank_account import BankAccount

class Bank:
    accounts = {}
    def __init__(self, bank_name: str, accounts: dict[str, BankAccount]): 
        self.bank_name = bank_name
        self.accounts = accounts if accounts is not None else {}
        
    def __str__(self):
        return f"Bank: {self.bank_name} | Accounts: {len(self.accounts)}"
    
    def add_account(self, account: BankAccount):
        self.accounts[account.account_number] = account
        return f"New account added for {account.owner_name} with account_number {account.account_number}."
    
    def get_account(self, account_number: str) -> BankAccount:
        return self.accounts.get(account_number)
    
    def show_all_accounts(self):
        for account in self.accounts.values():
            print(account)
    
    def save_all_accounts(self, filename: str):
        filename = f"{filename}.json"
        with open(filename, 'w') as file:
            data = [account.__dict__ for account in self.accounts.values()]
            json.dump(data, file, indent=4)
    
    def load_all_accounts(self, filename: str):
        filename = f"{filename}.json"
        with open(filename, 'r') as file:
            data = json.load(file)
            for account_data in data:
                account = BankAccount(**account_data)
                self.add_account(account) 
                
account1 = BankAccount("ACC001", "Alice", 500.0)
    print(account1)