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
class User:
    def __init__(self, name, email_address):# now our method has 2 parameters!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.BankAccount = BankAccount() # added association 
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        #change .deposit  to .balance :.balance is an attribute of the current child and .deposit is an attribute of the associated class, what ed do is exchange the method of the current class with a similar method from the class it is associated with, that it should iherti that specific method from
        
        self.balance.deposit += amount	# the specific user's account decreases by the amount of the value withdrawn, balance is an attribute 
    def make_withdrwal(self, amount):	# takes an argument that is the amount of the deposit
        if self.balance.withdraw-amount>=0:                    #as long as there is some money, withdraw money
            self.balance -= amount	# the specific user's account decreases by the amount of the value withdrawn
        else:
            print("Dear Mr.",self.name," ,you tried to withdraw: ",amount, "but you have insufficient balance so your withdrawal has failed. Your current balance is: ",self.account_balance)
    def display_user_balance(self):	# takes an argument that is the amount of the deposit
        pass    	# the specific user's account decreases by the amount of the value withdrawn
    def transfer_money_to_other_user(self,other,amount):	# takes an arguments self, other relates to other user and the amount to be transferred
        if self.balance - amount >=0:               #this is to check if the user got enough money
            self.balance-=amount
            other.balance+=amount
            print("success. Dear",self.name,", you have transferred an amount of: ",amount," to ",other.name,". Your current Balancec is",self.account_balance)
        else:
            print("Failed. Dear",self.name,", you have tried to transfer an amount of: ",amount," to ",other.name,"but your balance is insufficient.Your current Balancec is",self.account_balance)


me = User("fatima","mail@gmail.com")
me.BankAccount.deposit(34343)
me.BankAccount.withdraw(34343)
me.BankAccount.display_account_info()