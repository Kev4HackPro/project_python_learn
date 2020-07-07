class Account:
    """A class that prints out account details of a customer"""
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        print(f'New account created')
        cls.instance_count += 1

    def __init__(self, ac_no, ac_holder, opening_balance, ac_type):
        Account.increment_instance_count()
        self.ac_no = ac_no
        self.ac_holder = ac_holder
        self.balance = opening_balance
        self.ac_type = ac_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self,  amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'[{self.ac_no}]-{self.ac_holder}, {self.ac_type}={self.balance}'


acc1 = Account('447865', 'James Kariuki', 97678, 'current')
print(acc1)
acc2 = Account('445678', 'Anita Grande', 89789, 'savings')
print(acc2)
acc3 = Account('456754', 'Amina Abdi', 45678, 'investment')
print(acc3)
acc1.deposit(789000)
acc1.withdraw(654300)
print('Balance remaining:', acc1.get_balance())
print(f'Accounts created are {Account.instance_count}')