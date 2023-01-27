class Bank_account:
    accounts = []
    def __init__(self,interest_rate,balance):
        self.interest_rate= interest_rate
        self.balance = balance
        Bank_account.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insuffient funds")
        else:
            self.balance -= amount
            print(f"Balance ${self.balance}")
        return self

    def display_account_info(self):
        print("---------------------")
        print(f"Interest Rate - {self.interest_rate}")
        print(f"Balance - ${self.balance}")
        print("---------------------")
        return self

    def yield_interest(self):
        while self.balance > 0:
            self.balance *= 1.002
            return self

    @classmethod
    def print_account_info(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = {}

    def open_new_account(self,int_rate,account_name, balance):
        new_account = Bank_account(int_rate,balance)
        self.accounts[account_name] = new_account
        return self

#Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self, amount,account_name):
        self.accounts[account_name].deposit(amount)
        print(self.accounts[account_name].balance)
        return self
#Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdraw(self,amount,account_name):
        self.accounts[account_name].withdraw(amount)
        print(self.accounts[account_name].balance)
        return self
#Add a display_user_balance method to the User class that displays user's account balance
    def display_user_balance(self,account_name):
        print("---------------------")
        print(f"{self.first_name} {self.last_name}")
        print(f'{account_name} account')
        print(f"Balance - {self.accounts[account_name].balance}")
        print("---------------------")
        return self
#Add transfer method
    def transfer(self,amount,from_account,user, to_account):
        self.accounts[from_account].balance -= amount
        user.accounts[to_account].balance += amount
        return self


jon=User("jon", "jones", "jjones@jjj.com")
conor=User("conor", "mcgregor", "cm@cmc.com")
jon.open_new_account(0.01, "checkings", 100).open_new_account(0.02, "savings", 200).make_deposit(150, "checkings").display_user_balance("checkings").display_user_balance("savings")
conor.open_new_account(0.01,"checkings",50).open_new_account(0.02, "savings", 300).make_withdraw(200, "savings").display_user_balance("savings")
jon.transfer(100,"savings", conor, "savings").display_user_balance("savings")
conor.display_user_balance("savings")




