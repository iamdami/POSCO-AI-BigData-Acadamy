class BankAcc:
    def __init__(self, bal=0, name="none"):
        self.name = name
        self.bal = 0
        
    def deposit(self, amount):
        self.bal += amount
        
    def withdraw(self, amount):
        if amount >= self.bal:
            self.bal -= amount
    def transfer(self, other, amount):
        if self.bal < amount:
            print("잔고 부족. 잔액: ", self.bal)
        else:
            self.withdraw(amount)
            other.withdraw(amount)
            print("이체 성공. 잔액: ", self.bal)
            
acc1 = BankAcc(1)
acc2 = BankAcc(2)

acc1.deposit(400)
acc2.deposit(1000)

acc1.transfer(acc2, 1000)
acc2.transfer(acc1, 1000)
