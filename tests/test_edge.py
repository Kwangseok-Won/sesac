# 엣지 케이스 — 정상값만 테스트는 테스트가 아니다
# 초보가 가장 흔히 놓치는 것이 엣지 케이스(edge case)입니다.
# 버그는 대개 평범한 값이 아니라 경계에서 터져요
# — 딱 경곗값, 빈 값, 0, 음수 같은 극단에서요.
# 정상값만 넣어보는 건 테스트가 아니라 시연에 가깝습니다. "될 만한 것만 보여주는" 거죠.


def grade(score: int):
    if score < 0 or score > 100:
        return "범위를 벗어났습니다"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "F"


# 정상값
assert grade(95) == "A"
assert grade(85) == "B"

# 경계값 — 딱 90, 딱 80, 그리고 한 끗 아래 89
assert grade(90) == "A"
assert grade(80) == "B"
assert grade(89) == "B"

# 0 · 음수 같은 극단값
assert grade(0) == "F"
assert grade(-5) == "범위를 벗어났습니다"
assert grade(101) == "범위를 벗어났습니다"
print("정상·경계·극단까지 모두 통과 ✓")
