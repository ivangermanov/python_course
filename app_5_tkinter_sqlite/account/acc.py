class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account objects"""

    type = "checking"
    
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
    
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("account\\balance.txt", 1)
checking.deposit(10)
print(checking.balance)
checking.commit()

print(checking.__doc__)