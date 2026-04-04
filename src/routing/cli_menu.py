from domain.exceptions.insufficient_funds_error import InsufficientFundsError
from domain.exceptions.invalid_amount_error import InvalidAmountError
from persistence.bank_repository import BankRepository
from service.bank_service import BankService

def main():
    repo = BankRepository()
    service = BankService(repo)

    while True:
        print("\n=== SecureBank Menu ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Save Bank Data")
        print("6. Load Bank Data")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        # ---------------------------------------------------------
        # CREATE ACCOUNT
        # ---------------------------------------------------------
        if choice == "1":
            acc_num = input("Account Number: ").strip()
            name = input("Owner Name: ").strip()

            try:
                starting = float(input("Starting Balance: ").strip())
                service.create_account(acc_num, name, starting)
                print("Account created successfully.")
            except ValueError:
                print("Invalid starting balance. Please enter a number.")

        # ---------------------------------------------------------
        # DEPOSIT
        # ---------------------------------------------------------
        elif choice == "2":
            acc_num = input("Account Number: ").strip()

            try:
                amount = float(input("Deposit Amount: ").strip())
                new_balance = service.deposit(acc_num, amount)
                print(f"Deposit successful. New balance: ${new_balance:.2f}")
            except KeyError as e:
                print(str(e))
            except InvalidAmountError as e:
                print("Invalid amount:", e)
            except ValueError:
                print("Please enter a valid number.")

        # ---------------------------------------------------------
        # WITHDRAW
        # ---------------------------------------------------------
        elif choice == "3":
            acc_num = input("Account Number: ").strip()

            try:
                amount = float(input("Withdrawal Amount: ").strip())
                new_balance = service.withdraw(acc_num, amount)
                print(f"Withdrawal successful. New balance: ${new_balance:.2f}")
            except KeyError as e:
                print(str(e))
            except InsufficientFundsError as e:
                print("Transaction failed:", e)
            except InvalidAmountError as e:
                print("Invalid amount:", e)
            except ValueError:
                print("Please enter a valid number.")

        # ---------------------------------------------------------
        # CHECK BALANCE
        # ---------------------------------------------------------
        elif choice == "4":
            acc_num = input("Account Number: ").strip()

            try:
                acc = service.get_account(acc_num)
                print(f"Balance: ${acc.balance:.2f}")
            except KeyError as e:
                print(str(e))

        # ---------------------------------------------------------
        # SAVE BANK DATA
        # ---------------------------------------------------------
        elif choice == "5":
            filename = input("Save to filename: ").strip()
            service.save_bank(filename)
            print("Bank data saved.")

        # ---------------------------------------------------------
        # LOAD BANK DATA
        # ---------------------------------------------------------
        elif choice == "6":
            filename = input("Load from filename: ").strip()
            service.load_bank(filename)
            print("Bank data loaded.")

        # ---------------------------------------------------------
        # EXIT
        # ---------------------------------------------------------
        elif choice == "7":
            print("Thank you for using SecureBank. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()

