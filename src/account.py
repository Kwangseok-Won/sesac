class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount}원 입금 → 잔액 {self.balance}원")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("실행 거부.\n사유: 액수 초과")
        else:
            self.balance = self.balance - amount
            print(f"{amount}원 인출 → 잔액 {self.balance}원")


cheolsoo = Account("철수", 1000)
yeonghui = Account("영희", 2000)

cheolsoo.deposit(500)
cheolsoo.withdraw(2000)
cheolsoo.withdraw(300)

print("-" * 40)

yeonghui.deposit(500)
yeonghui.withdraw(2000)
yeonghui.withdraw(300)
