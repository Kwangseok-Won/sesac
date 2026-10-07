# 데코레이터 — 함수를 선물상자로 포장하기
# 먼저 알아둘 것 — 파이썬에서 함수는 일급 객체(first-class object)입니다. 함수를 변수에 담고, 다른 함수의 인자로 넘기고, 함수에서 반환할 수 있어요. (앞에서 sorted(key=lambda ...)로 함수를 인자로 넘긴 게 이미 그 예입니다.)
# 데코레이터(decorator)는 기존 함수를 감싸(wrapping) 기능을 더하는 문법입니다 — 선물을 그대로 두고 포장지만 씌우는 것과 같아요. 원래 함수는 건드리지 않고, 실행 전후에 로그·시간 측정·권한 검사 같은 일을 덧붙입니다. 함수 정의 위에 @데코레이터이름을 붙이면 끝이에요.


# ① 함수는 일급 객체 — 변수에 담을 수 있다
def shout(text):
    return text.upper() + "!"


say = shout  # 함수 자체를 변수에 담기
print(say("hello"))  # HELLO!


# ② 데코레이터: 함수를 인자로 받아, 감싼 함수를 반환
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"[호출] {func.__name__}")
        result = func(*args, **kwargs)  # 원래 함수 실행
        print(f"[완료] {func.__name__} -> {result}")
        return result

    return wrapper


# ③ @로 포장 — add를 logged로 감싼다
@logged
def add(a, b):
    return a + b


print(add(3, 4))
