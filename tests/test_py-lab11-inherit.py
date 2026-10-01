from ..src.py-lab11-inherit import Animal, Cat, Dog, Puppy, chorus


def test_부모가_이름을_기억한다():
    assert Animal("흰둥이").name == "흰둥이"
    assert Animal("흰둥이").speak() == "..."


def test_사람이_읽는_모양():
    assert str(Animal("흰둥이")) == "동물 흰둥이"


def test_물려받는다():
    assert issubclass(Dog, Animal) and issubclass(Cat, Animal)
    assert Dog("바둑이").name == "바둑이", "이름은 부모가 처리한다 — 다시 쓰지 않는다."


def test_덮어쓴다():
    assert Dog("바둑이").speak() == "멍멍"
    assert Cat("나비").speak() == "야옹"


def test_손자도_이름을_받는다():
    puppy = Puppy("콩이", 1)
    assert puppy.name == "콩이", "super().__init__() 을 불렀는지 보세요."
    assert puppy.age == 1


def test_super_로_부모의_소리를_쓴다():
    assert Puppy("콩이", 1).speak() == "멍멍!", (
        '"멍멍!" 을 직접 쓰지 말고 super().speak() 에 "!" 를 붙이세요. '
        "Dog 의 소리가 바뀌면 Puppy 도 따라와야 합니다."
    )


def test_같은_함수가_다르게_동작한다():
    animals = [Dog("바둑이"), Cat("나비"), Puppy("콩이", 1)]
    assert chorus(animals) == "멍멍 야옹 멍멍!"


def test_str_이_상속된다():
    assert str(Dog("바둑이")) == "동물 바둑이"
