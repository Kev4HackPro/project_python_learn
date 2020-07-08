class Account:

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        print('New Account Created')
        cls.instance_count += 1

    def __init__(self, account_number, account_holder, opening_balance, type_of_account):
        Account.increment_instance_count()
        self.ac_no = account_number
        self.ac_holder = account_holder
        self._balance = opening_balance
        self.type = type_of_account

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f'[{self.ac_no}] {self.ac_holder} {self.type}={self._balance}'


class CurrentAccount(Account):

    def __init__(self, account_number, account_holder, opening_balance, overdraft_limit):
        super().__init__(account_number, account_holder, opening_balance, 'current account')
        self.ovdrft_limit = -overdraft_limit

    def withdraw(self, amount):
        if self.ovdrft_limit > self._balance - amount:
            print('Withdrawal will exceed your overdraft limit')
        else:
            self._balance -= amount

    def __str__(self):
        return f'{super().__str__()}, overdraft_limit = {self.ovdrft_limit}'


class DepositAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, interest_rate):
        super().__init__(account_number, account_holder, opening_balance, 'deposit account')
        self.interest = interest_rate

    def __str__(self):
        return f'{super().__str__()} interest_rate={self.interest}'


class InvestmentAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, investment_type):
        super().__init__(account_number, account_holder, opening_balance, 'investment account')
        self.investment = investment_type

    def __str__(self):
        return f"{super().__str__()} investment_type = {self.investment}"


acc1 = CurrentAccount('789006', 'James Maina Kariuki', 97000, 600000)
print(acc1)
acc2 = DepositAccount('456789', 'Eunice Nyasuguta', 45978, 0.12)
print(acc2)
acc3 = InvestmentAccount('4467865', 'Marion Karanja', 560000, 'safe')
print(acc3)

acc1.deposit(450000)
acc1.withdraw(78000)
print('Balance', acc1.balance)
acc1.withdraw(7900000)
print('Balance is', acc1.balance)