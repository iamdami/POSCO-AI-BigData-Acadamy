class bankAcount:
    def __init__(self, num, rate=0.01):
        self.num = num
        self.bal = 0
        self.rate = rate

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount

    def obtainInterest(self):
        self.bal += self.bal + self.rate

    def transfer(self, other, amount):
        if self.bal < amount:
            print("잔고가 부족합니다. 잔액 = ", self.bal)
        else:
            self.withdraw(amount)
            other.deposit(amount) 
            print("이체 성공. 잔액 = ", self.bal)

acc1 = bankAcount(1001)
acc2 = bankAcount(1002)
acc3 = bankAcount(1003)

acc1.deposit(500)
acc2.deposit(1000)

acc1.transfer(acc2, 1000)
acc2.transfer(acc1, 1000)
