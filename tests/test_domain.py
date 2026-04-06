# Test Cases
from domain.bank_account import BankAccount
from domain.exceptions.insufficient_funds_error import InsufficientFundsError
from domain.exceptions.invalid_amount_error import InvalidAmountError
from persistence.bank_repository import BankRepository
from domain.bank import Bank

#Test 1: Basic Account Creation
print("Test 1: Basic Account Creation")
acc = BankAccount("ACC001", "Alice", 500.00)
assert str(acc) == "Account: [ACC001] | Owner: Alice] | Balance: $500.00"
assert repr(acc) == "BankAccount(account_number='ACC001', owner_name='Alice', balance=500.00)"
print("Test sat!")

#Test 2: Valid Deposit
print("Test 2: Valid Deposit")
acc.make_deposit(250)
assert acc.balance == 750.0
print("Test sat!")

#Test 3: Valid Withdrawal
print("Test 3: Valid Withdawl")
acc.make_withdrawl(100)
assert acc.balance == 650.0
print("Test sat!")

# Test 8: Bank Class
print("Test 8: Bank Class")
bank = Bank("SecureBank", {})
bank.add_account(BankAccount("ACC003", "Carol", 300.0))
bank.add_account(BankAccount("ACC004", "Dave", 800.0))
assert len(bank.accounts) == 2
print("Test sat!")

# Test 9: Get Non-Existent Account
print("Test 9: Get Non-Existent Account")
try:
    bank.get_account("ACC999")
    assert False, "Should have raised KeyError"
except KeyError:
    pass # Correct!
print("Test sat!")





