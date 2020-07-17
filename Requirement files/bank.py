class Bank():
    def __init__(self,balance):
        self.balance=balance

    def debit(self,amount):
        if amount is None:
            raise TypeError
        if amount<0:
            return -1
        if amount>self.balance:
            return 0
        self.balance-=amount

    def credit(self,amount):
        if amount is None:
            raise TypeError
        if amount<0:
            return -1
        self.balance+=amount
    
    def get_balance(self):
        return self.balance
    
    