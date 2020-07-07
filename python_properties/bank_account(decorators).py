class Account:
    """" A class used to represent a type of account """

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        print('Creating new Account')
        cls.instance_count += 1

    def __init__(self, account_number, account_holder, opening_balance, account_type):
        Account.increment_instance_count()
        self.account_number = account_number
        self.account_holder = account_holder
        self._open_bal = opening_balance
        self.type = account_type

    def deposit(self, amount):
        self._open_bal += amount

    def withdraw(self, amount):
        self._open_bal -= amount

    @property
    def balance(self):
        """Provides current balance"""
        return self._open_bal

    def __str__(self):
        return f'Account[{self.account_number}] - {self.account_holder}, {self.type} account ={self._open_bal}'


class CurrentAccount(Account):

    def __init__(self, account_number, account_holder, opening_balance, overdraft_limit):
        super().__init__(account_number, account_holder, opening_balance, 'current')
        self.overdraft_limit = -overdraft_limit

    def withdraw(self, amount):
        if self._open_bal - amount < self.overdraft_limit:
            print('Withdrawal would exceed your overdraft limit')
        else:
            self._open_bal -= amount

    def __str__(self):
        return f'{super().__str__()} overdraft limit:{self.overdraft_limit}'


class DepositAccount(Account):

    def __init__(self, account_number, account_holder, opening_balance, interest_rate):
        super().__init__(account_number, account_holder, opening_balance, 'deposit')
        self.interest_rate = interest_rate

    def __str__(self):
        return f'{super().__str__()}  interest rate: {self.interest_rate}'


class InvestmentAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, investment_type):
        super().__init__(account_number, account_holder, opening_balance, 'investment')
        self.investment_type = investment_type

    def __str__(self):
        return f"{super().__str__()} type:{self.type}"


acc1 = CurrentAccount('123', 'Kavita', 23450, 100000)
print(acc1)
acc2 = DepositAccount('345', 'Kavita', 23550, 0.5)
print(acc2)
acc3 = InvestmentAccount('567', 'Sunaina', 12450, 'high risk')
print(acc3)

acc1.deposit(23490)
acc1.withdraw(12330)
print('balance:', acc1.balance)

print('Number of Account instances created:', Account.instance_count)

print('balance:', acc1.balance)
acc1.withdraw(300000.00)
print('balance:', acc1.balance)
