def add(a, b):
    return a + b


def test_add_positive():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


# pytest가 자동으로 하는 일을 직접 호출로 흉내내기
test_add_positive()
test_add_zero()
print("2개 테스트 통과 — pytest라면 자동으로 찾아 돌려줬을 것")
