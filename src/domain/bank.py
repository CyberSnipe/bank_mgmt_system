import json
from .bank_account import BankAccount

# TASK 6: Bank Class
class Bank:
    """Class representing a bank with multiple accounts."""
    
    # Constructor to initialize the bank with a name and an optional dictionary of accounts
    def __init__(self, bank_name: str, accounts: dict[str, BankAccount]):
        """Constructor to initialize the bank with a name and an optional dictionary of accounts."""
        # TODO: Add account to self.accounts using account_number as key
        # Hint: self.accounts[account.account_number] = account
        self.bank_name = bank_name
        self.accounts = accounts if accounts is not None else {}
    
    # String representation of the bank showing its name and the number of accounts    
    def __str__(self):
        """String representation of the bank showing its name and the number of accounts."""
        return f"Bank: {self.bank_name} | Accounts: {len(self.accounts)}"
    
    # Official representation of the bank showing its name and accounts in a more detailed format
    def __repr__(self):
        """Representation of the bank showing its name and accounts in a more detailed format."""
        return f"Bank(bank_name='{self.bank_name}', accounts={self.accounts})"
    
    def add_account(self, account: BankAccount):
        """Adds a new account to the bank's accounts dictionary using the account number as the key."""
        self.accounts[account.account_number] = account
        return f"New account added for {account.owner_name} with account_number {account.account_number}."
    
    def get_account(self, account_number: str) -> BankAccount | None:
        """Gets an account from the bank's accounts dictionary using the account number as the key. Returns None if the account does not exist."""
        # TODO: Check if account_number is in self.accounts
        # TODO: If not found, raise KeyError with a friendly message
        # TODO: If found, return the account
        
        return self.accounts.get(account_number)
        
    def show_all_accounts(self):
        """Shows all accounts in the bank by printing their string representations."""
        # TODO: If no accounts, print "No accounts found."
        # TODO: Otherwise, print each account using its __str__
        
        for account in self.accounts.values():
            print(account)
    
    def save_all_accounts(self, filename: str):
        """Saves all accounts in the bank to a JSON file. The filename is given as an argument and the .json extension is added automatically."""
        # TODO: Open filename in write mode inside a try block
        # TODO: Write each account as: account_number,owner_name,balance
        # TODO: Catch IOError and print an error message
        
        filename = f"{filename}.json"
        with open(filename, 'w') as file:
            data = [account.__dict__ for account in self.accounts.values()]
            json.dump(data, file, indent=4)
    
    @classmethod
    def load_all_accounts(cls, filename, bank_name="LoadedBank"):
        """
        Loads all accounts from a JSON file and adds them to the bank's accounts dictionary. 
        The filename is given as an argument and the .json extension is added automatically.
        """
        # TODO: Create a new Bank object using cls(bank_name)
        # TODO: Open the file and read line by line
        # TODO: For each line, split by "," and create a BankAccount
        # TODO: Add each account to the bank's accounts dictionary
        # TODO: Catch FileNotFoundError — print message, return empty bank
        # TODO: Catch ValueError — print message, return empty bank
        # TODO: Return the bank object
        
        filename = f"{filename}.json"
        with open(filename, 'r') as file:
            data = json.load(file)
            for account_data in data:
                account = BankAccount(**account_data)
                self.add_account(account) 
                
account1 = BankAccount("ACC001", "Alice", 500.0)
print(account1)