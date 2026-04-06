from persistence.bank_repository import BankRepository
from service.bank_service import BankService
from routing.cli_menu import main as cli_main

def main():
    repo = BankRepository()
    service = BankService(repo)

    # Load seed data
    service.load_all_accounts("data/seed_account_repo.json")

    # Start CLI
    cli_main()

   
if __name__ == "__main__":
    main()

