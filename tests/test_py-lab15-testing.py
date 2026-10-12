import pytest

from py_lab15_testing import cases, grade, invalid_inputs


# 일부러 망가뜨린 구현들. 여러분의 cases() 가 이것들을 잡아내야 합니다.
def bug_boundary(score):  # ① 경계를 > 로 썼다
    if score > 90:
        return "A"
    if score > 80:
        return "B"
    if score > 70:
        return "C"
    return "F"


def bug_missing_c(score):  # ② C 를 빠뜨렸다
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    return "F"


def bug_reversed(score):  # ③ 순서를 뒤집었다
    if score >= 70:
        return "C"
    if score >= 80:
        return "B"
    if score >= 90:
        return "A"
    return "F"


def catches(broken):
    """내 테스트가 이 구현의 버그를 잡아내는가."""
    return any(broken(score) != expected for score, expected in cases())


def test_케이스가_비어_있지_않다():
    assert len(cases()) >= 4


def test_바른_구현은_다_통과한다():
    for score, expected in cases():
        assert grade(score) == expected, f"{score} 의 기대값이 틀렸습니다"


def test_경계_버그를_잡는다():
    assert catches(bug_boundary), "90 을 넣어보세요"


def test_빠진_등급을_잡는다():
    assert catches(bug_missing_c), "70~79 구간을 넣어보세요"


def test_뒤집힌_순서를_잡는다():
    assert catches(bug_reversed), "90 이상을 넣어보세요"


def test_범위_밖_입력을_모았다():
    assert len(invalid_inputs()) >= 2


def test_범위_밖은_정말_오류를_낸다():
    for value in invalid_inputs():
        with pytest.raises(ValueError):
            grade(value)


def test_양쪽_끝을_다_봤다():
    assert any(v < 0 for v in invalid_inputs()), "0 보다 작은 값도 넣으세요"
    assert any(v > 100 for v in invalid_inputs()), "100 보다 큰 값도 넣으세요"
