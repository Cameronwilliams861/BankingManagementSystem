class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self,customer):
        self.customers.append(customer)

    def find_customer(self,customer_id):
        #AI says this should be a for loop instead because it doesn't handle error handling well
        if customer_id in self.customers:
            print(f"{customer_id} in our database")

    def get_all_customers(self):
        print("These are the list of the people in the customer database")
        for i in range (len(self.customers)):
            print(f"{self.customers[i]}")

    def generate_bank_report(self):
        print(f"At {self.bank_name} we have the following individuals currently registered: ")
        self.get_all_customers()