# https://pilab-textbook.fly.dev/#/python/ch11_oop

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
