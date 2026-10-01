# https://pilab-textbook.fly.dev/#/python/ch11_oop

PI = 3.14


class Shape:
    """
    종합 예제 — 도형 클래스
        상속·super·오버라이딩·__str__을 한데 엮어, 도형 클래스를 만듭니다.

    Shape가 공통(이름·str)을 담고, 각 도형이 area를 오버라이딩합니다.
    부모의 __str__은 self.area()를 부르는데, 실제로는 각 자식의 area가 실행돼요
    — 같은 print 코드가 도형마다 알맞게 동작합니다. 이게 객체지향의 우아함입니다.
    """

    def __init__(self, name: str):
        self.name = name

    def area(self):
        return 0

    def __str__(self) -> str:
        return f"{self.name}의 넓이: {self.area()}"


class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        super().__init__("직사각형")
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("원")
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2


class Triangle(Shape):
    def __init__(self, w: float, h: float):
        super().__init__("삼각형")
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h / 2


# __str__ 덕분에 print가 깔끔
print(Rectangle(4, 5))  # 직사각형의 넓이: 20
print(Circle(3))  # 원의 넓이: 28.26
print(Triangle(4, 5))
