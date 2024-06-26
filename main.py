from account_management.account import Account
from account_management.customer import Customer
from transaction_processing.transaction import Transaction
from transaction_processing.transaction_processor import TransactionProcessor

##Create customer
customer1=Customer("C001","Diksha Kamble")
customer2=Customer("C002","Karan Kulkarni")

##Create accounts
account1=Account("A001",customer1)
account2=Account("A002",customer2,balance=5000.0)

##Display Intial Balance
print(f"{customer1.name}'s Balance:{account1.get_balance()}")
print(f"{customer2.name}'s Balance:{account2.get_balance()}")

##Perform transaction
transaction1=Transaction("T001",account1,"deposit",1000.0)
transaction2=Transaction("T002",account2,"withdraw",1500.0)

TransactionProcessor.process_transaction(transaction1)
TransactionProcessor.process_transaction(transaction2)

##Display updated balance
print(f"{customer1.name}'s Updated Balance:{account1.get_balance()}")
print(f"{customer2.name}'s Updated Balance:{account2.get_balance()}")

