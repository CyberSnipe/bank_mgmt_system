from domain.bank_account import BankAccount

class Bank:
    """Domain model representing a bank that manages multiple accounts."""

    def __init__(self, bank_name: str, accounts: dict[str, BankAccount] | None = None):
        self.bank_name = bank_name
        self.accounts = accounts if accounts is not None else {}

    def __str__(self):
        return f"Bank: {self.bank_name} | Accounts: {len(self.accounts)}"

    def __repr__(self):
        return f"Bank(bank_name='{self.bank_name}', accounts={self.accounts})"
    
    # ---------------------------------------------------------
    # ACCOUNT MANAGEMENT
    # ---------------------------------------------------------

    def add_account(self, account: BankAccount):
        """Add a new account to the bank."""
        self.accounts[account.account_number] = account

    def get_account(self, account_number: str) -> BankAccount:
        """Retrieve an account or raise KeyError if not found."""
        if account_number not in self.accounts:
            raise KeyError(f"Account '{account_number}' not found.")
        return self.accounts[account_number]
    
    def list_accounts(self):
        """Return a list of accounts (no printing)."""
        return list(self.accounts.values())  
    

    

