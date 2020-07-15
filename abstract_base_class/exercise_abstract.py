from abstract_base_class.fintech.account_abstract import *

customer1 = CurrentAccount('12345', 'James Kariuki', 85670, 500000)
print(customer1)
customer2 = InvestmentsAccount('47894', 'Wayne Makau', 45678, 'risky')
print(customer2)
customer3 = SavingsAccount('23456', 'Omondi James', 904589, 0.5)
print(customer3)

customer1.deposit(23490)
customer1.withdraw(12330)
print(f'balance remaining at {customer1.acc_hold} account:', customer1.balance)

print('Number of Account instances created:', Account.instance_count)
try:
    print('balance:', customer1.balance)
    customer1.withdraw(30000000.00)
    print('new balance:', customer1.balance)
except BalanceError as e:
    print('Handling Exception')
    print(e)

try:
    customer1.branch(100)
    print(customer1.balance)
except AmountError as e:
    print(e)