from customer import Customer


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self,customer):
        self.customers.append(customer)
        #print(self.customers)

    def find_customer(self,customer_id):
        #AI says this should be a for loop instead because it doesn't handle error handling well
        for i in range (len(self.customers)):
            #print(self.customers[i].customer_id)
            if self.customers[i].customer_id == customer_id:

                return self.customers[i]

        return None

    def get_all_customers(self):
        print("These are the list of the people in the customer database")
        #for i in range (len(self.customers)):
        #    print(f"{self.customers[i].}")
        acc = 1
        for customer in self.customers:
            #print(f"Name: {customer.name} \nCustomer ID: {customer.customer_id} \nCustomer Email: {customer.email} \nNumber of Accounts: {len(customer.accounts)}")
            print(f"Customer {acc}")
            print(customer.get_customer_info())
            acc +=1

    def generate_bank_report(self):
        print(f"At {self.bank_name} we have the following individuals currently registered: ")
        self.get_all_customers()
