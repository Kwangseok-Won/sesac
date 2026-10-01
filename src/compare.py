# 중간에 print·여러 작업이 섞이거나 로직이 복잡할 때
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

print(squares)

# 읽는 법 — [i**2 for i in range(1,6)]은 "range(1,6)의 각 i에 대해, i**2를 모아 리스트로"라고 읽습니다.
# [결과식 for 변수 in 반복대상] 구조예요. 만들 값을 앞에 쓰는 게 포인트입니다.
#
# 어울리는 상황: 단순한 변형·거르기 — "리스트 → 리스트"가 명확할 때
print([i ** 2 for i in range(1, 6)])
