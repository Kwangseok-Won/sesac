# https://pilab-textbook.fly.dev/#/python/ch04c_tuple
t1 = (1, 2, 3)
t2 = 1, 2, 3
t3 = ("철수", 25, True)
empty = ()

print(type(t2))
print(t3)

# 흔한 실수 — 요소 1개짜리 튜플
#
# 요소가 하나면 쉼표를 꼭 붙여야 튜플이 됩니다. (5)는 그냥 숫자 5이고, (5,)여야 튜플입니다. 쉼표가 튜플을 만든다는 걸 여기서 다시 확인하세요.
print(1)
print((1,))
print(type((1,)))
