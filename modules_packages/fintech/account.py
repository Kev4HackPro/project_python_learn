class BalanceError(Exception):

    def __init__(self, account):
        self.account = account


class AmountError(Exception):

    def __init__(self, account, msg):
        self.account = account
        self.msg = msg

    def __str__(self):
        return f'AmountError: {self.msg} on {self.account}'


class Account:
    instance_count = 0

    @classmethod
    def instance_count_method(cls):
        print('New account created')
        cls.instance_count += 1

    def __init__(self, acc_no, acc_hold, open_bal, acc_type):
        Account.instance_count_method()
        self.acc_no = acc_no
        self.acc_hold = acc_hold
        self._open_bal = open_bal
        self.acc_type = acc_type

    def deposit(self, amount):
        if amount < 0:
            raise AmountError(account=self, msg='You cannot deposit negative amounts')
        else:
            self._open_bal += amount

    def withdraw(self, amount):
        if amount < 0:
            raise AmountError(self, 'Cannot withdraw negative amount')
        else:
            self._open_bal -= amount

    @property
    def balance(self):
        current_bal = self._open_bal
        return current_bal

    def __str__(self):
        return f"Bank account [{self.acc_no}] of {self.acc_hold} which has {self._open_bal}." \
               f" Type of account: {self.acc_type} account. "


class CurrentAccount(Account):

    def __init__(self, acc_no, acc_hold, open_bal, ovdrft_lmt):
        super().__init__(acc_no, acc_hold, open_bal, 'current')
        self.ovdrft = -ovdrft_lmt

    def withdraw(self, amount):
        if amount < 0:
            raise AmountError(self, 'Cannot withdraw negative amounts')
        elif self.ovdrft > self._open_bal - amount:
            print('Overdraft limit reached')
        else:
            self._open_bal -= amount

    def __str__(self):
        return f"{super().__str__()} overdraft limit{self.ovdrft}"


class InvestmentsAccount(Account):
    def __init__(self, acc_no, acc_hold, open_bal, investment_type):
        super().__init__(acc_no, acc_hold, open_bal, 'investments')
        self.invest = investment_type

    def __str__(self):
        return f"{super().__str__()} type of investment:" \
               f"{self.invest}"


class SavingsAccount(Account):

    def __init__(self, acc_no, acc_hold, open_bal, int_rate):
        super().__init__(acc_no, acc_hold, open_bal, 'savings')
        self.int_rate = int_rate

    def __str__(self):
        return f"{super().__str__()} interest_rate {self.int_rate}"
