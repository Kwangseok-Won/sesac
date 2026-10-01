# k:v 유형이면 dict이고, k만 있으면 set

person = {"name": "철수", "age": 25}
# person["phone"]처럼 없는 key를 대괄호로 찾으면 KeyError가 납니다.
# 있을지 없을지 모르면 get()을 쓰세요 — 없으면 None(또는 지정한 기본값)을 돌려줘 안전합니다.
print(person.get("phone", "없음"))
