# 심화 — 왜 self를 첫 인자로 꼬박꼬박 쓸까

# d.bark()는 사실 파이썬이 속으로 Dog.bark(d)로 바꿔 부릅니다 — 점(.) 앞의 d가 첫 인자로 자동 전달되는 거예요.
# 그래서 메서드 정의의 첫 자리에 그걸 받을 self가 반드시 필요합니다. 깜빡하면 "인자 개수가 안 맞는다"는 에러가 나죠.
# 이름이 꼭 self여야 하는 문법은 아니지만(첫 인자면 무엇이든 됨), 모두가 self로 쓰기로 약속했기에 관례를 따릅니다.
# 핵심은 이것 — "이 메서드가 어느 인스턴스의 것인지"를 self가 알려주기에, 같은 bark 코드 한 벌로 바둑이도 뽀삐도 각자 짖을 수 있습니다.


class Dog:
    """
    https://pilab-textbook.fly.dev/#/python/ch10_class
    """

    def __init__(self, name, age):
        """속성 설정"""

        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: 멍멍!")

    def who_ami_i(self):
        print(f"self의 주소: {id(self)}")

    def get_info(self):
        return f"{self.name}, {self.age}살"

    def birthday(self):  # 나이 +1 (자기 속성 변경)
        self.age = self.age + 1
        print(f"{self.name} 생일! 이제 {self.age}살")


baduk = Dog("바둑이", 3)
ppoppi = Dog("뽀삐", 2)
print(baduk.name)
print(baduk.age)
baduk.bark()

baduk.who_ami_i()
print(f"baduk의 주소: {id(baduk)}")
