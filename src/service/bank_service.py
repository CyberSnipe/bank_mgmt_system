from domain.bank import Bank
from domain.bank_account import BankAccount
from domain.exceptions.invalid_amount_error import InvalidAmountError
from domain.exceptions.insufficient_funds_error import InsufficientFundsError
from persistence.bank_repository import BankRepository

class BankService:
    """Service layer for orchestrating bank operations."""

    def __init__(self, bank_repository: BankRepository, bank_name: str = "SecureBank"):
        self.bank_repository = bank_repository
        self.bank = Bank(bank_name)

    # ---------------------------------------------------------
    # ACCOUNT MANAGEMENT
    # ---------------------------------------------------------

    def create_account(self, account_number: str, owner_name: str, balance: float = 0.0):
        account = BankAccount(account_number, owner_name, balance)
        self.bank.add_account(account)
        return account

    def get_account(self, account_number: str) -> BankAccount:
        return self.bank.get_account(account_number)

    # ---------------------------------------------------------
    # TRANSACTIONS
    # ---------------------------------------------------------

    def deposit(self, account_number: str, amount: float) -> float:
        account = self.get_account(account_number)
        new_balance = account.make_deposit(amount)
        return new_balance

    def withdraw(self, account_number: str, amount: float) -> float:
        account = self.get_account(account_number)
        new_balance = account.make_withdrawl(amount)
        return new_balance

    # ---------------------------------------------------------
    # PERSISTENCE
    # ---------------------------------------------------------

    def save_bank(self, filename: str):
        """Save all accounts to JSON via the repository."""
        self.bank_repository.save_all(self.bank, filename)

    def load_bank(self, filename: str):
        """Load all accounts from JSON via the repository."""
        self.bank = self.bank_repository.load_all(filename, self.bank.bank_name)
        return self.bank

    # ---------------------------------------------------------
    # QUERIES
    # ---------------------------------------------------------

    def list_accounts(self):
        """Return all accounts (domain objects)."""
        return self.bank.list_accounts()

