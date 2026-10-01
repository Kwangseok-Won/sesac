# 중요 — 순서가 결과를 바꾼다
#
# elif는 위에서부터 확인하고 처음 참인 곳에서 멈춥니다.
# 그래서 85점은 >=90(거짓)을 지나 >=80(참)에서 멈춰 "B"가 됩니다.
# 만약 >=70을 맨 위에 두면 85점도 "C"가 돼버려요.
# 범위 조건은 큰 값부터, 좁은 조건부터 배치하는 게 안전합니다.

score = 85

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# else:
#     grade = "F"

# if 70 <= score < 80:
#     grade = "C"
# elif 80 <= score < 90:
#     grade = "B"
# elif score >= 90:
#     grade = "A"
# else:
#     grade = "F"

# if 70 <= score and score < 80:
#     grade = "C"
# elif score >= 80 and score < 90:
#     grade = "B"
# elif score >= 90:
#     grade = "A"
# else:
#     grade = "F"

if score < 70:
    grade = "F"
elif score < 80:
    grade = "C"
elif score < 90:
    grade = "B"
else:
    grade = "A"

print(f"점수 {score} -> 학점 {grade}")
