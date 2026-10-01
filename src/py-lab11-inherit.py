# https://pilab-textbook.fly.dev/#/python/lab/py-lab11-inherit

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

    def __str__(self):
        return f"동물 {self.name}"          # "동물 흰둥이"


class Dog(Animal):
    def speak(self) -> str:
        return "멍멍"


class Cat(Animal):
    def speak(self) -> str:
        return "야옹"


class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)                 # 부모의 준비를 먼저
        self.age = age

    def speak(self) -> str:
        return super().speak() + "!"          # 부모의 소리 뒤에 "!"


def chorus(animals: list[Animal]) -> str | None:
    """동물들의 소리를 공백으로 이어 붙인다."""
    return " ".join(animal.speak() for animal in animals)

    # 이렇게 하면 채점 기준에 안 맞는 듯
    # speak = ""
    # for animal in animals:
    #     speak += animal.speak() + " "
    #
    # return speak


whitey = Animal("흰둥이")
badook = Dog("바둑이")
nahbii = Cat("나비")
kongii = Puppy("콩이", 1)

for a in whitey, badook, nahbii, kongii:
    print(a, "-", a.speak())

print(chorus([whitey, badook, nahbii, kongii]))
