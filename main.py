from customer import Customer
from account import Account
from transaction import Transaction
from bank import Bank

#Test to see if adding Cameron works, and it did!
bank1 = Bank("Chase Morgan")

bank1.add_customer("Cameron")
bank1.add_customer("Jack")
bank1.add_customer("Kallie")

bank1.find_customer("Cameron")

#bank1.get_all_customers()

bank1.generate_bank_report()

account1 = Account(account_number="1234", account_type="savings", balance=50000)

account1.deposit(5000)

#account1.get_transactions()

account1.withdraw(5000)

account1.get_transactions()