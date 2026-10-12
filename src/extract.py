# https://pilab-textbook.fly.dev/#/python/ch14_regex

# 실전 패턴 — 이메일·전화번호
# 4b장 종합 예제에서 split("@")로 이메일 하나를 갈랐죠.
# 하지만 긴 글 속에 흩어진 여러 개를 한꺼번에 뽑으려면 정규식이 제격입니다.
# 이메일의 모양은 글자들 @ 글자들 — 이를 [\w.]+@[\w.]+로 그립니다
# ([\w.]는 "글자 또는 점", +는 "1개 이상").

# 두 가지 쓰임에 주목하세요.
# findall은 긴 글에서 맞는 조각을 추출하고, fullmatch는 "이 문자열 전체가 형식에 맞나?"를 검증합니다.
# "010-12-5678"은 가운데가 4자리가 아니라 False
# — 회원가입 폼의 형식 검사가 이렇게 돌아갑니다.

import re

text = "문의: hong@example.com / 010-1234-5678, 이수진 sujin.lee@example.co.kr"

emails = re.findall(r"[\w.]+@[\w.]+", text)
phones = re.findall(r"\d{3}-\d{4}-\d{4}", text)
print(emails)
print(phones)

print(bool(re.fullmatch(r"\d{3}-\d{4}-\d{4}", "010-1234-5678")))
print(bool(re.fullmatch(r"\d{3}-\d{4}-\d{4}", "010-12-5678")))
