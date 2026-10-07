# https://pilab-textbook.fly.dev/#/python/ch11_oop

# 심화 — 상속은 언제 쓰나: "is-a" 관계
# 상속을 쓸지 판단하는 기준은 "자식은 부모의 한 종류인가?"(is-a)입니다.
# "전사는 캐릭터다", "원은 도형이다" — 이렇게 말이 되면 상속이 자연스럽습니다.
# 반대로 "자동차는 엔진이다"는 어색하죠(엔진은 자동차의 부품).
# 이럴 땐 상속이 아니라 속성으로 가지는(has-a) 게 맞아요(self.engine = Engine()).
# 상속의 진짜 목적은 코드 재사용을 넘어, "이 자식들은 모두 부모 타입"이라는 공통 규격을 세우는 것
# — 그래서 §6처럼 같은 코드로 여러 도형을 다룰 수 있습니다.


class Character:
    """
    부모 클래스 - 모든 캐릭터의 공통
    """

    def __init__(self, name):
        self.name = name
        self.hp = 100

    def info(self):
        print(f"{self.name} (HP {self.hp})")

    def attack(self):
        print("기본 공격!")


class Warrior(Character):
    """
    자식 클래스 - Character를 물려받음
    """

    def attack(self):
        """
        자식에 같은 이름의 메서드가 있으면 자식 것이 우선 호출됩니다.
        부모의 원래 동작도 함께 쓰고 싶으면 오버라이딩한 메서드 안에서 super().attack()을 부르면 돼요.
        """
        print(f"{self.name}: 칼을 휘두른다!")
        print("강력한 검격! (3배 데미지)")  # 같은 이름 → 덮어씀


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)  # 부모의 초기화 먼저 (name, hp 설정)
        self.mp = 50  # 마법사만의 속성 추가


arthur = Warrior("아서")
arthur.info()  # 물려받은 메서드 → 아서 (HP 100)
arthur.attack()  # 강력한 검격! (자식 것이 우선)
Character("기본").attack()  # 기본 공격!

gandalf = Mage("간달프")
print(gandalf.name, gandalf.hp, gandalf.mp)  # 간달프 100 50
