import account


class Customer:
    def __init__(self, name, customer_id, email):
        self.name = name
        self.customer_id = customer_id
        self.email = email
        self.accounts = []

    def add_account(self,account):
        self.accounts.append(account)
    def get_customer_info(self):
        print(f"Name: {self.name}\nCustomer ID: {self.customer_id}\nEmail: {self.email}")
        #print(self.get_accounts())
    def get_accounts(self):
        for accounts in self.accounts:
            print(accounts)