# 평범한 함수
def square(side: float) -> float:
    return side ** 2

# 언제 쓰나 — 람다는 다른 함수에 잠깐 건넬 때 빛납니다.
# 변수에 담아 이름 붙일 거면(square2 = lambda...) 그냥 def를 쓰는 게 낫습니다.
square_lambda = lambda side: side ** 2
print(square(5))
print("-" * 40)
print(square_lambda(5))
