class BankAccount:
    interest=1
    rate=1
    balance=0
    def __init__(self, int_rate=1, balance=0):
        self.rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        self.balance-=amount
    def display_account_info(self):
        print("Account info:","--interest:",self.interest,"--rate:",self.rate,"--balance:",self.balance) #\n new line
    def yield_interest(self):
        self.balance*=self.rate

bank_abc = BankAccount(0.5,2000)
bank_xyz = BankAccount(0.02,5000)
bank_abc.deposit(100)
bank_abc.deposit(330)
bank_abc.deposit(7956)
bank_abc.withdraw(645)
bank_abc.yield_interest()
bank_abc.display_account_info()
bank_xyz.deposit(100)
bank_xyz.deposit(330)
bank_xyz.withdraw(76)
bank_xyz.withdraw(645)
bank_xyz.withdraw(300)
bank_xyz.yield_interest()
bank_xyz.display_account_info()

