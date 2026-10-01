# https://pilab-textbook.fly.dev/#/python/ch08_function

# ② return이 없으면 자동으로 None을 반환합니다. print만 하는 함수의 반환값을 변수에 담으면 None이 들어갑니다.
def greet(name: str) -> None: # parameter;매개변수
    print(f"{name}님, 안녕하세요!")


greet("철수") # argument;전달인자
greet("영희")


def add(a: float, b: float) -> None:
    print(f"{a} + {b} = {a + b}")


add(3, 5)
