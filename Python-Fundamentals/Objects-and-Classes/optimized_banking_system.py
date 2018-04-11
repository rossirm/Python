from decimal import Decimal


class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance

    def get_info(self):
        return f'{self.name} -> {self.balance:.2f} ({self.bank})'


def create_accounts(storage):
    line = input()
    while line != 'end':
        bank, name, balance = line.split(' | ')
        storage.append(BankAccount(name, bank, Decimal(balance)))
        line = input()
    return storage


def sort_accounts(storage):
    sorted_accounts = sorted(storage, key=lambda account: (account.balance, -len(account.bank)), reverse=True)
    return sorted_accounts


def print_info(accounts):
    for account in accounts:
        print(account.get_info())


data_base = []
create_accounts(data_base)

print_info(sort_accounts(data_base))
