# https://pilab-textbook.fly.dev/#/python/ch14_regex

# re.search(패턴, 글) — 패턴에 맞는 첫 부분 하나를 찾음 (없으면 None)
# re.findall(패턴, 글) — 맞는 부분을 모두 리스트로
# re.sub(패턴, 바꿀말, 글) — 맞는 부분을 치환

# 아래는 문장에서 숫자 덩어리를 찾는 예제입니다. \d는 '숫자 한 개', +는 '1개 이상'을 뜻해요(다음 절에서 정리). 즉 \d+는 "숫자가 이어진 덩어리"입니다.

# search는 매치 객체를 돌려주므로, 실제 글자를 얻으려면 .group()을 붙입니다. findall은 곧바로 리스트를, sub는 바뀐 새 문자열을 돌려줘요 (원본은 그대로 — 문자열은 불변, 4b장!). 예상 출력은 마지막 줄이 주문번호 #, 금액 #원, 수량 #개입니다.

import re

text = "주문번호 12045, 금액 3800원, 수량 2개"

print(re.search(r"\d+", text).group())  # 첫 숫자 덩어리 → 12045
print(re.findall(r"\d+", text))  # 전부 → ['12045', '3800', '2']
print(re.sub(r"\d+", "#", text))  # 숫자를 #으로 가림
