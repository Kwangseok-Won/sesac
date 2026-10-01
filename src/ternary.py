# 남용은 금물 — 한 줄이 멋져 보이지만, 조건이 복잡하면 오히려 읽기 어렵습니다. "값 하나를 간단히 정할 때"만 쓰고, 복잡하면 일반 if-else로 풀어 쓰는 게 좋습니다.

score = 50

# 일반 if-else
if score >= 60:
    result = "합격"
else:
    result = "불합격"

# ternary
result = "합격" if score >= 60 else "불합격"
print(result)

grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(grade)
