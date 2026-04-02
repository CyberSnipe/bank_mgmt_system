from src.domain.exceptions.insufficient_funds_error import InsufficientFundsError
from src.domain.exceptions.invalid_amount_error import InvalidAmountError
from src.domain.bank_account import BankAccount
from src.domain.bank import Bank
from src.service.bank_service import BankService




# Bank Management System
# TASK 7: Main Menu
import os
import json

def main():
    bank = Bank("SecureBank")
    #TODO: Load existing accounts from a file if it exists (use Bank.load_all_accounts)

    while True:
        print("SecureBank Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Save Bank Data")
        print("6. Load Bank Data")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            acc_num = input("Account Number: ").strip()
            name = input("Owner Name: ").strip()
            try:
                starting = float(input("Starting Balance: ").strip())
                # TODO: Create a BankAccount and add it to the bank
            except ValueError:
                print("Invalid starting balance. Please enter a number.")

        elif choice == "2":
            acc_num = input("Account Number: ").strip()
            try:
                # TODO: Get the account using bank.get_account()
                # TODO: Get the deposit amount from user (convert to float)
                # TODO: Call deposit() and print new balance
                pass
            except KeyError as e:
                print(str(e))
            except InvalidAmountError as e:
                print("Invalid amount: " + str(e))
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            acc_num = input("Account Number: ").strip()
            try:
                # TODO: Get the account using bank.get_account()
                # TODO: Get the withdrawal amount from user (convert to float)
                # TODO: Call withdraw() and print new balance
                pass
            except KeyError as e:
                print(str(e))
            except InsufficientFundsError as e:
                print("Transaction failed: " + str(e))
            except InvalidAmountError as e:
                print("Invalid amount: " + str(e))
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            acc_num = input("Account Number: ").strip()
            try:
                # TODO: Get the account and print its balance
                pass
            except KeyError as e:
                print(str(e))

        elif choice == "5":
            filename = input("Save to filename: ").strip()
            # TODO: Call bank.save_all_accounts(filename)

        elif choice == "6":
            filename = input("Load from filename: ").strip()
            # TODO: Call Bank.load_all_accounts() and reassign bank

        elif choice == "7":
            print("Thank you for using SecureBank. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()