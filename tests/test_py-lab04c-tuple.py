from ..src/py-lab04c-tuple import count_and_find, first_and_rest, single, swap, try_change


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
