# 흔한 실수 — range는 끝 숫자를 포함하지 않는다
#
# range(5)는 0~4(5개), range(1, 6)은 1~5입니다. 끝 숫자는 포함되지 않아요
# — 3장 슬라이싱과 같은 규칙입니다. "1부터 10까지"는 range(1, 11)이에요.
#
# 증가폭에 음수를 주면 거꾸로 셉니다. range(10, 0, -1)은 10, 9, ..., 1이에요. end=" "는 print가 줄바꿈 대신 공백으로 끝나게 하는 옵션인데, 지금은 몰라도 됩니다.

# ① range(횟수): 0부터 횟수-1까지
for i in range(5):
    print(i, end=" ")
print()

# ② range(시작, 끝): 시작부터 끝-1까지
for i in range(1, 6):
    print(i, end=" ")
print()

# ③ range(시작, 끝, 증가폭)
for i in range(0, 21, 5):
    print(i,end=" ")
