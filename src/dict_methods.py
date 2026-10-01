# https://pilab-textbook.fly.dev/#/python/ch05_mutable
person = {"name": "철수", "age": 25}

print(person.get("name"))

# 흔한 실수 — 없는 key를 대괄호로 찾기
#
# person["phone"]처럼 없는 key를 대괄호로 찾으면 KeyError가 납니다.
# 있을지 없을지 모르면 get()을 쓰세요 — 없으면 None(또는 지정한 기본값)을 돌려줘 안전합니다.
print(person.get("phone"))
print(person.get("phone", "없음"))

print(person.keys())
print(person.values())
print(person.items())

print("age" in person)
