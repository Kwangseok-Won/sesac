# for 실전 — 합계와 조건 결합
# 반복문의 진짜 힘은 조건문(6장)과 만날 때 나옵니다. 1부터 100까지 짝수의 합을 구해봅시다.
#
# 누적 패턴 — total = 0으로 시작해 반복마다 더해나가는 건 프로그래밍에서 가장 자주 쓰는 패턴입니다.
# total += i로 짧게 쓸 수도 있어요 (total = total + i를 줄여 쓴 '복합 할당 연산자'예요).

total = 0 # 짝수의 합
total_odd = 0 # 홀수의 합

for i in range(1, 101):
    if i % 2 == 0:
        total += i
    else:
        total_odd += i

print(f"1 - 100까지 짝수의 합: {total}") # 2550
print(f"1 - 100까지 홀수의 합: {total_odd}") # 2500
