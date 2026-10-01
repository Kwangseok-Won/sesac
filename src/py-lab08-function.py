def grade(score):
    """점수를 받아 등급 문자열('A'/'B'/'C'/'F')을 돌려줍니다."""
    # 여기를 완성하세요.
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


print(grade(90))
print(grade(89))
print(grade(80))
print(grade(70))
print(grade(69))
