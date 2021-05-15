class User:		# declare a class and give it name User
    name=""
    email=""
    account_balance=0
    def __init__(self,name,email,balance):
        self.name = name
        self.email = email
        self.account_balance =balance
    def deposit(self,amount):
        self.account_balance+=amount
        print("success, you added",amount,". Your current Balance is",self.account_balance)
    def withdrawal(self, amount):
        if amount<=self.account_balance:
            self.account_balance -= amount
        else:
            print("not enough")
    def display_user_balance(self):
        print("mr.",self.name,"has a balance of",self.account_balance)
#end of class
adam = User("Adam","adam@gmail.com",1000)
fatima = User("Fatima", "Fatima@gmail.com",1200)
mohammad = User("Mohammad","mohammad@gmail.com",1300)
adam.deposit(300)
adam.deposit(200)
adam.deposit(500)
adam.withdrawal(1)