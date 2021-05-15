class User:
    def __init__(self, name, email_address):# now our method has 2 parameters!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account decreases by the amount of the value withdrawn
    def make_withdrwal(self, amount):	# takes an argument that is the amount of the deposit
        if self.account_balance-amount>=0:                    #as long as there is some money, withdraw money
            self.account_balance -= amount	# the specific user's account decreases by the amount of the value withdrawn
        else:
            print("Dear Mr.",self.name," ,you tried to withdraw: ",amount, "but you have insufficient balance so your withdrawal has failed. Your current balance is: ",self.account_balance)
    def display_user_balance(self):	# takes an argument that is the amount of the deposit
        print ("Dear ",self.name," your current balance is: ",self.account_balance)     	# the specific user's account decreases by the amount of the value withdrawn
    def transfer_money_to_other_user(self,other,amount):	# takes an arguments self, other relates to other user and the amount to be transferred
        if self.account_balance - amount >=0:               #this is to check if the user got enough money
            self.account_balance-=amount
            other.account_balance+=amount
            print("success. Dear",self.name,", you have transferred an amount of: ",amount," to ",other.name,". Your current Balancec is",self.account_balance)
        else:
            print("Failed. Dear",self.name,", you have tried to transfer an amount of: ",amount," to ",other.name,"but your balance is insufficient.Your current Balancec is",self.account_balance)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
amy = User("Amy sherlock Holmes", "amy@mastermind.com")
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_withdrwal(50)
guido.display_user_balance()    #output: Dear  Guido van Rossum  your current balance is:  350
monty.make_deposit(50)
monty.make_deposit(150)
monty.make_withdrwal(100)
monty.make_withdrwal(101)       #output: Dear Mr. Monty Python  ,you tried to withdraw:  101 but you have insufficient balance so your withdrawal has failed. Your current balance is:  100
monty.display_user_balance()    #output: Dear  Monty Python  your current balance is:  100
amy.make_deposit(2500)
amy.make_withdrwal(230)
amy.make_withdrwal(500)
amy.make_withdrwal(999)
amy.display_user_balance()      #output: Dear  Amy sherlock Holmes  your current balance is:  771
amy.transfer_money_to_other_user(monty,700)
amy.transfer_money_to_other_user(guido,100)