import math  # math 모듈 전체 불러오기

print(math.sqrt(16))  # 제곱근 → 4.0
print(math.pi)  # 원주율 → 3.141592...

from math import sqrt  # 특정 기능만 콕 집어 불러오기

print(sqrt(25))  # math. 없이 바로 → 5.0

import math as m  # 별명 붙이기 (짧게)

print(m.floor(3.7))  # 내림 → 3
