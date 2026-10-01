class Dog:
    """
    https://pilab-textbook.fly.dev/#/python/ch10_class
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: 멍멍!")

    def who_ami_i(self):
        print(f"self의 주소: {id(self)}")


baduk = Dog("바둑이", 3)
ppoppi = Dog("뽀삐", 2)
print(baduk.name)
print(baduk.age)
baduk.bark()

baduk.who_ami_i()
print(f"baduk의 주소: {id(baduk)}")
