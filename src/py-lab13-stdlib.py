import math


def circle_area(r: float) -> float:
    """원의 넓이. 소수 둘째 자리에서 반올림."""
    return round(math.pi * r**2, 2)


def safe_divide(a, b) -> float | None:
    """0으로 나누면 None. 죽지 않는다."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_number(text) -> int | None:
    """정수로 바꾼다. 숫자가 아니면 None."""
    try:
        return int(text)
    except ValueError:
        return None
    except Exception as e:
        print(e)
        return None


def classify_error(fn):
    """fn 을 실행하고 난 에러의 이름을 돌려준다. 성공하면 '성공'."""

    try:
        fn()
        return "성공"
    except ZeroDivisionError:
        return "ZeroDivisionError"
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"
    except KeyError:
        return "KeyError"
    except Exception as e:
        return f"알 수 없는 에러: {type(e).__name__}"


def with_cleanup(fn, log: list[str]):
    """성공하든 실패하든 log 에 '정리' 를 넣는다."""
    try:
        result = fn()
    except Exception as e:
        print(e)
        return None
    else:
        return result
    finally:
        log.append("정리")


log: list[str] = []
print(with_cleanup(lambda: 7, log))
print(with_cleanup(lambda: 1 / 0, log))
print(log)


def raise_odd():
    raise IndexError("범위 밖")


print(classify_error(raise_odd))
