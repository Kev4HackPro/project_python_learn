class AmountError(Exception):
    """Prevents customers from depositing or withdrawing negative amounts"""
    def __init__(self, account, message):
        self.account = account
        self.msg = message

    def __str__(self):
        return f"'{self.msg} on {self.account}"


class BalanceError(Exception):
    """Makes sure customer does not withdraw beyond overdraft limit"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"You have reached your overdraft limit"


class Account:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        print('New Account created')
        cls.instance_count += 1

    def __init__(self, account_number, account_holder, balance,type_of_account):
        Account.increment_instance_count()
        self.ac_no = account_number
        self.ac_hold = account_holder
        self._balance = balance
        self.type = type_of_account

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise AmountError(account=self, message='cannot deposit negative amount')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise AmountError(self, 'cannot withdraw negative amounts')

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f" Account[{self.ac_no}] of {self.ac_hold} of type {self.type} has a balance of {self._balance}"


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance, 'current account')
        self.overdraft = -overdraft_limit

    def withdraw(self, amount):
        if amount < 0:
            raise AmountError(self, 'cannot withdraw negative amounts')
        elif self.overdraft > self._balance - amount:
            raise BalanceError(amount)
        else:
            self._balance -= amount

    def __str__(self):
        return f"{super().__str__()}, overdraft_limit = {self.overdraft}"


class DepositAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance, 'deposit account')
        self.interest = interest_rate

    def __str__(self):
        return f"{super().__str__()}, interest_rate = {self.interest}"


class InvestmentAccount(Account):
    def __init__(self, account_number, account_holder, balance, investment_type):
        super().__init__(account_number, account_holder, balance, 'investment account')
        self.investment = investment_type

    def __str__(self):
        return f"{super().__str__()}, investment_type= {self.investment}"


acc1 = CurrentAccount('4567890', 'Kimani Wambugu', 97000, 780000)
print(acc1)
acc2 = DepositAccount('67890567', 'Rufina Limbe', 67000, 0.12)
print(acc2)
acc3 = InvestmentAccount('234565', 'Brec Bassinger', 4500000, 'safe')
print(acc3)

acc1.deposit(60000)
acc1.withdraw(78000)
print('Balance:', acc1.balance)
acc1.withdraw(45670)
print('Balance', acc1.balance)
try:
    acc1.deposit(-1)
    print('balance', acc1.balance)
except AmountError as e:
    print(e)
try:
    print('balance:', acc1.balance)
    acc1.withdraw(678900)
    print('balance:', acc1.balance)
except BalanceError as e:
    print(e)


