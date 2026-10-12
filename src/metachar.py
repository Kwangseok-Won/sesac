# https://pilab-textbook.fly.dev/#/python/ch14_regex

# 비유 — 종류(\d \w \s)와 양( + ? {})은 짝*
# 메타문자는 두 축으로 나뉩니다. "어떤 글자냐"(\d=숫자, \w=글자, .=아무거나)와 "몇 번이냐"(*=0개+, +=1개+, ?=0~1개)입니다.
# 이 둘을 붙이면 문장이 됩니다 — \d+는 "숫자를 1개 이상", \w{3}는 "글자를 정확히 3개". 종류 + 양, 이 조합이 패턴의 뼈대예요.

import re

print(re.findall(r"\d", "a1b2c3"))  # 숫자 하나씩 → ['1', '2', '3']
print(re.findall(r"\w+", "hi, there!"))  # 단어 덩어리 → ['hi', 'there']
print(re.findall(r"\s", "a b\tc"))  # 공백류 → [' ', '\t']
print(re.findall(r"[aeiou]", "banana"))  # 모음 집합 → ['a', 'a', 'a']
print(re.search(r"colou?r", "color").group())  # u가 0~1개 → color
