def single(value: int) -> tuple[int]:
    """값 하나만 담은 튜플. (3) 은 튜플이 아니다 — 쉼표가 튜플을 만든다."""
    return value,


def swap(a: int, b: int) -> tuple[int, int]:
    """두 값을 맞바꾼다. 임시 변수 없이 한 줄."""
    return b, a


def first_and_rest(items: list[int]) -> tuple[int, list[int]]:
    """(첫 값, 나머지 리스트). * 를 쓰면 한 줄."""
    first, *rest = items
    return first, rest


def count_and_find(items: tuple[int], target: int) -> tuple[int, int]:
    """(몇 개, 첫 위치). 없으면 (0, -1)."""
    if target not in items:
        return 0, -1
    return items.count(target), items.index(target)


def try_change(items: tuple[int]):
    """튜플의 첫 원소를 바꿔본다. 실패하면 '바꿀 수 없음'."""
    try:
        items[0] = 0 # Tuples don't support item assignment
    except Exception as e:
        print(e)
        print(type(e).__name__) # 예외 이름을 알아내기
        return
    # except TypeError: # 특정 에러
    #     return "바꿀 수 없음"


def test_원소_하나짜리_튜플():
    result = single(3)
    assert isinstance(result, tuple), "(3) 은 튜플이 아닙니다. 쉼표가 튜플을 만듭니다."
    assert result == (3,)
    assert len(result) == 1


def test_문자열도_된다():
    assert single("가") == ("가",)


def test_맞바꾸기():
    assert swap(1, 2) == (2, 1)
    assert swap("a", "b") == ("b", "a")


def test_첫_값과_나머지():
    assert first_and_rest([1, 2, 3, 4]) == (1, [2, 3, 4])
    assert first_and_rest([9]) == (9, [])


def test_세고_찾는다():
    assert count_and_find((1, 2, 2, 3, 2), 2) == (3, 1)
    assert count_and_find((1, 2, 3), 9) == (0, -1)


def test_튜플은_바뀌지_않는다():
    assert try_change((1, 2, 3)) == "바꿀 수 없음", (
        "튜플은 원소를 바꿀 수 없습니다. TypeError 가 납니다."
    )


test_원소_하나짜리_튜플()
test_문자열도_된다()
test_맞바꾸기()
test_첫_값과_나머지()
test_세고_찾는다()
test_튜플은_바뀌지_않는다()
