# 제너레이터 — 값을 하나씩 내주는 함수
#
# 지금까지 컴프리헨션은 리스트를 통째로 만들어 메모리에 쌓았습니다. 제너레이터(generator)는 반대예요
# — yield로 값을 필요할 때 하나씩 내줍니다. 함수 안에 return 대신 yield가 있으면 그 함수는 제너레이터가 됩니다.
#
# 비유 — 리스트는 뷔페 접시에 음식을 전부 담아놓는 것이고, 제너레이터는 주문할 때마다 한 접시씩 내주는 주방입니다.
# 100만 개를 다뤄도 한 번에 하나씩만 만들므로 메모리를 거의 쓰지 않아요.

def squares_gen(side):
    for i in range(side):
        yield i ** 2

# 알아서 하나씩 꺼냄
for x in squares_gen(4):
    print(x)

print("-" * 40)

gen = squares_gen(4)
print(next(gen))
print(next(gen))
print(next(gen))

print("-" * 40)

# generator expression - Comprehension의 소괄호 버전
generator_expression_squared = (side ** 2 for side in range(5))
print(sum(generator_expression_squared))
