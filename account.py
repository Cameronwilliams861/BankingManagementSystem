import transaction


class Account:
    def __init__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({"AccountNumber": self.account_number})
        self.transactions.append({"TransactionType": "deposit"})
        self.transactions.append({"totalAmount": amount})
        self.transactions.append({"Balance": self.balance},)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, you don't have enough money")
            self.get_balance()
        else:
            self.balance -= amount
            self.transactions.append({"TransactionType": "withdraw"},)

    def get_balance(self):
        print(f"{self.balance} is your balance.")

    def get_transactions(self):
        for transaction in self.transactions:
            print(transaction)