# 흔한 실수 — 기본값은 뒤쪽에
#
# 기본값이 있는 매개변수는 없는 것보다 뒤에 와야 합니다. def f(a=1, b)는 에러예요. def f(b, a=1)처럼 써야 합니다.
# "기본값 없는 것 먼저, 있는 것 나중에"로 기억하세요.
# def greet(greeting="안녕하세요", name: str) -> None:

def greet(name: str, greeting="안녕하세요") -> None:
    print(f"{name}님, {greeting}!")


greet("철수")
greet("영희", "반가워요")

# 키워드 인자: 이름을 지정해 전달 (순서 자유)
greet(greeting="환영합니다", name="민수")
