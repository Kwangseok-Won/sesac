# 실행할 때마다 random 결과가 달라집니다. 여러 번 실행해 보세요.
# 7장의 숫자 맞히기 게임에서 정답을 random.randint(1, 100)으로 바꾸면 진짜 게임이 됩니다.

import math
import random

print(math.ceil(3.2))
print(math.floor(3.8))
print(math.gcd(12, 18))

print(random.randint(1, 6))
print(random.choice(["가위", "바위", "보"]))

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(nums)
