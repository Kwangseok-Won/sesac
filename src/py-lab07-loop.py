# sales 가 주어집니다. 직접 시험해보려면 아래 줄의 # 을 지우세요.
sales = [45_000, 120_000, 98_000, 150_000]

total = 0
big_days = 0
best = 0
worst = 999_999 # 큰 수로 초기화

for amount in sales:
    total += amount

    if amount >= 100_000:
        big_days += 1

    if best < amount: # max()를 쓰지 않고 최대치를 구하는 방법
        best = amount

    if worst > amount:
        worst = amount

print(total, big_days, best, worst)
