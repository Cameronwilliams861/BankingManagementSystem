
from bank import Bank
from customer import Customer
from account import Account
from transaction import Transaction


# ==================================
# TEST 1: Create the bank
# ==================================

bank = Bank("First National Bank")

print("\n--- BANK TEST ---")
print(f"Bank Name: {bank.bank_name}")


# ==================================
# TEST 2: Create customers
# ==================================

customer1 = Customer("John Smith", 101, "john@email.com")
customer2 = Customer("Jane Doe", 102, "jane@email.com")

bank.add_customer(customer1)
bank.add_customer(customer2)

print("\n--- CUSTOMER TEST ---")
print(f"Number of customers: {len(bank.customers)}")

assert len(bank.customers) == 2


# ==================================
# TEST 3: Find a customer
# ==================================

found_customer = bank.find_customer(101)


print("\n--- FIND CUSTOMER TEST ---")

if found_customer:
    print(f"Found: {found_customer.name}")
else:
    print("Customer not found")

assert found_customer.customer_id == 101

# Test an ID that doesn't exist
missing_customer = bank.find_customer(999)

assert missing_customer is None


# ==================================
# TEST 4: Create accounts
# ==================================

account1 = Account(50001, "Checking", 1000)
account2 = Account(50002, "Savings", 5000)
account3 = Account(50003, "Checking", 2500)

customer1.add_account(account1)
customer1.add_account(account2)
customer2.add_account(account3)

print("\n--- ACCOUNT TEST ---")

assert len(customer1.accounts) == 2
assert len(customer2.accounts) == 1

print(f"{customer1.name} has {len(customer1.accounts)} accounts.")
print(f"{customer2.name} has {len(customer2.accounts)} accounts.")


# ==================================
# TEST 5: Deposit money
# ==================================

print("\n--- DEPOSIT TEST ---")

account1.deposit(500)

print(f"Expected balance: 1500")
print(f"Actual balance: {account1.balance}")

assert account1.balance == 1500


# ==================================
# TEST 6: Withdraw money
# ==================================

print("\n--- WITHDRAWAL TEST ---")

account1.withdraw(200)

print(f"Expected balance: 1300")
print(f"Actual balance: {account1.balance}")

assert account1.balance == 1300


# ==================================
# TEST 7: Insufficient funds
# ==================================

print("\n--- INSUFFICIENT FUNDS TEST ---")

account1.withdraw(5000)

print(f"Expected balance: 1300")
print(f"Actual balance: {account1.balance}")

assert account1.balance == 1300


# ==================================
# TEST 8: Transaction history
# ==================================

print("\n--- TRANSACTION HISTORY TEST ---")

account1.get_transactions()


# ==================================
# TEST 9: Bank report
# ==================================

print("\n--- BANK REPORT TEST ---")

bank.generate_bank_report()


print("\nAll tests completed!")
