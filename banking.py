class BankAccount:
    interest_rate = 0.04    # class variable
    def __init__(self, name, balance):
        # instance variables
        self.name = name
        self.balance = balance
        self.transactions = [ ]     # every bank customer will get an empty list as soon as bank account is opened
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"amount deposited {amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        self.balance = self.balance - amount
        self.transactions.append(f"amount withdrawn {amount}")
    
    def transfer(self, to_account, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds")
        to_account.deposit(amount)  # transferring the amount to "c2"
        self.withdraw(amount)    # decudting the amount from "c1"
        self.transactions.append(f"Amount transferred {amount}")
    
    def roi(self):
        int_amount = self.balance * self.interest_rate
        self.deposit(int_amount)
