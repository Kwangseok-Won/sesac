# https://pilab-textbook.fly.dev/#/python/ch11_oop

class Account:
    """
    캡슐화 — 속성 보호

    10장 은행 계좌에서 acc.balance = 999999처럼 밖에서 잔액을 맘대로 바꿀 수 있었죠. 위험합니다.
    캡슐화는 "이 속성은 함부로 건드리지 마세요"를 표시하는 관례예요.

    밑줄의 의미(관례) — 속성 앞 밑줄 하나(_balance)는 "내부용이니 밖에서 직접 쓰지 말자"는 약속입니다(강제는 아님).
    밑줄 둘(__balance)은 더 강하게 숨깁니다(이름이 바뀜).
    핵심은 "검증을 거치는 메서드로만 바꾸게 해서 데이터를 안전하게" 지키는 것이에요.
    """
    def __init__(self, balance: int):
        self._balance = balance  # 밑줄 1개 = "내부용, 직접 건드리지 마"

    def deposit(self, amount: int):
        if amount > 0:  # 검증을 거쳐야만 변경 가능
            self._balance += amount

    def withdraw(self, amount: int):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print(f"액수를 다시 확인하십시오.\n현재 잔액: {self._balance}")

    def get_balance(self):
        return self._balance


acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500 (메서드를 통해서만 접근)

acc.withdraw(700)
print(acc.get_balance())

acc.withdraw(1000)
print(acc.get_balance())
