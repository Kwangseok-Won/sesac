# 심화 — 람다는 언제 쓰고, 언제 def로 돌아가나
#
# 람다에는 일부러 만든 제약이 있습니다.
# ① 이름이 없고, ② 몸통은 식(expression) 하나뿐이라
# if 블록·for·여러 줄·return 여러 개를 담을 수 없어요. 이건 단점이 아니라 용도입니다
# — "정렬 기준 하나", "요소 하나를 변형" 같은 짧은 일회용 함수를 그 자리에서 건넬 때 쓰라는 뜻이죠.
# 그래서 sorted(students, key=lambda s: s[1])처럼 인자로 넘기는 자리가 람다의 진짜 집이에요
# — 이름 붙일 필요 없이 그 줄에서 태어나 그 줄에서 쓰이고 사라집니다.
# 반대로 재사용해야 하거나, 로직이 두 줄을 넘거나, 이름이 있어야 읽기 쉬운 함수는 8장의 def로 돌아가세요.
# square2 = lambda x: x**2처럼 람다에 이름을 붙이는 순간, 그건 def square2(x):를 어렵게 돌려 쓴 것일 뿐
# — 파이썬 스타일 가이드도 이 경우 def를 권합니다.

students = [("철수", 85), ("영희", 92), ("민수", 78)]

by_score_asc = sorted(students, key=lambda student: student[1])
print(by_score_asc)

from_top = sorted(students, key=lambda student: student[1], reverse=True)
print(from_top)
