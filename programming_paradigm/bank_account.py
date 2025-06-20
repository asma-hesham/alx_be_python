class BankAccount:
    def __init__(self,inital_balance=0):
        self.__account_balance = inital_balance
    def deposit(self,amount):
        if amount > 0:
            self.__account_balance += amount
    def withdraw(self,amount):
        if 0<amount<=self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print (f"current Balance: {self.__account_balance:.2f}")
