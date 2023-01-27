class Bank_account:
    accounts = []
    def __init__(self,first_name, last_name,interest_rate,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.interest_rate= interest_rate
        self.balance = balance
        Bank_account.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -+ amount
        return self

    def display_account_info(self):
        print("---------------------")
        print(f"First Name - {self.first_name}")
        print(f"Last Name - {self.last_name}")
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


user1 = Bank_account("Conor", "Mcgregor", 0.002, 0)
user2 = Bank_account("Max", "Halloway", 0.002, 0)

user1.display_account_info().deposit(10000).deposit(15000).deposit(8000).withdraw(12000).yield_interest().display_account_info()
user2.display_account_info().deposit(3000).deposit(9000).withdraw(2000).withdraw(2500).withdraw(5000).withdraw(7500).yield_interest().display_account_info()

Bank_account.print_account_info()