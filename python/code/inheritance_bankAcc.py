class BankAcc:
    def __init__(self, bal=0, name="none"):
        self.name = name
        self.bal = bal
        
    def deposit(self, amount):
        self.bal += amount
        
    def withdraw(self, amount):
        if amount >= self.bal:
            self.bal -= amount

    def transfer(self, amount):
        if self.bal < amount:
            print("잔고 부족. 잔액: ", self.bal)
        else:
            self.withdraw(amount)
            print("이체 성공. 잔액: ", self.bal)

class minBankAcc(BankAcc):
    def __init__(self, bal=0, name="none", minBal = 0):
        super().__init__(bal, name)
        self.minBal = minBal

    def withdraw(self, amount):
        if self.bal - amount < self.minBal:
            print("출금못함.")
        else:
            self.withdraw(amount)

acc = minBankAcc(500, "kim", 1000)
acc.deposit(1000)
acc.withdraw(600)
