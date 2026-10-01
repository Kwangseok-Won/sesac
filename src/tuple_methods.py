# https://pilab-textbook.fly.dev/#/python/ch04c_tuple

t = (1, 2, 2, 3, 2, 3)
print(t.count(2))
print(t.index(3))

print("-" * 40)

# 찾는 숫자가 여러 개일 경우 index 여러 개 출력
for idx, element in enumerate(t):
    if element == 3:
        print(f"{element}의 인덱스: {idx}")

print("-" * 40)

for i in range(len(t)):
    if t[i] == 3:
        print(f"{t[i]}의 인덱스: {i}")
