# BankAccount Class
from domain.exceptions.invalid_amount_error import InvalidAmountError
from domain.exceptions.insufficient_funds_error import InsufficientFundsError

class BankAccount:
    """Domain Class representing a bank account."""

    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def __str__(self):
        return f"Account: [{self.account_number}] | Owner: {self.owner_name} | Balance: ${self.balance:.2f}"

    def __repr__(self):
        return (
            f"BankAccount(account_number='{self.account_number}', "
            f"owner_name='{self.owner_name}', balance={self.balance})"
        )

    def make_deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def make_withdrawl(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount
        return self.balance

