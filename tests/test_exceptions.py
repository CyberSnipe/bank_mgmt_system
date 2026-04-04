from domain.bank_account import BankAccount
from domain.exceptions.insufficient_funds_error import InsufficientFundsError
from domain.exceptions.invalid_amount_error import InvalidAmountError
from persistence.bank_repository import BankRepository
from domain.bank import Bank
from service.bank_service import BankService


# Test 4: Insufficient Funds
print("Test 4: Insufficient Funds")
try:
    BankAccount.make_withdrawl(9999)
    assert False, "Should have raised InsufficientFundsError"
except InsufficientFundsError:
    pass

try:
    BankAccount.make_deposit(-100)
    assert False, "Should have raised InvalidAmountError"
except InvalidAmountError:
    pass

