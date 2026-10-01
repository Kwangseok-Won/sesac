# 주의 — 뒤의 if(거르기) vs 앞의 if-else(선택)
#
# 거르기는 for 뒤에: [x for x in ... if 조건] (조건 맞는 것만 남김).
# 값 바꾸기는 앞에 삼항으로: ["짝" if x%2==0 else "홀" for x in ...] (6장 삼항 연산자). 위치가 다르니 헷갈리지 마세요.

print([even for even in range(10) if even % 2 == 0])
print([natural * 2 for natural in range(-5, 11) if natural > 0])
print([conditional_even for conditional_even in range(10) if conditional_even < 5 if conditional_even % 2 == 0])
print(["짝" if conditional % 2 == 0 else "홀" for conditional in range(10) if conditional < 5])


print("-" * 40)

evens = []
for even in range(10):
    if even % 2 == 0:
        evens.append(even)

print(evens)


naturals = []
for natural in range(-5, 11):
    if natural > 0:
        naturals.append(natural * 2)

print(naturals)


conditional_evens = []
for conditional_even in range(10):
    if conditional_even % 2 == 0 and conditional_even < 5:
        conditional_evens.append(conditional_even)

print(conditional_evens)

evens_odds = []
for number in range(10):
    if number < 5:
        evens_odds.append("짝" if number % 2 == 0 else "홀")

print(evens_odds)
