# break와 continue — 반복 제어
#
# 반복 도중 빠져나오거나(break), 이번 회차만 건너뛸(continue) 수 있습니다.

for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ") # 1 2 3 4
print()

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, end=" ") # 1 3 5 7 9
