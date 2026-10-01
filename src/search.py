s = "banana"

print(s.find("a")) # 첫 'a'의 위치 → 1
print(s.find("z")) # 없으면 → -1

# 핵심 차이 — find는 -1, index는 에러
#
# 찾는 글자가 없을 때 동작이 다릅니다. find()는 조용히 -1을 돌려주지만, index()는 ValueError 에러를 냅니다.
# "있는지 없는지 모를 땐 find, 반드시 있다고 확신하면 index"로 기억하세요.
# 위 코드에서 s.index("z")를 추가해 직접 에러를 확인해 보세요.

print(s.index("a")) # 첫 'a'의 위치 → 1

print(s.count("a")) # 'a' 개수 → 3


# 특정 문자열 있는 지 확인 후 index 반환
ch = input("특정 문자열 있는 지 확인 후 index 반환: ")
if s.find(ch) == 1: # -1도 truthy이기 때문에 == 1이라고 정확하게 비교연산을 해야 한다
    print(s.index(f"{ch}의 위치: {s.index(ch)}"))
else:
    print("없다")


# 방법	무엇을 돌려주나	못 찾으면	언제 쓰나
# s.find("a")	첫 위치(정수)	-1 (조용히)	위치가 필요한데 없을 수도 있을 때
# s.index("a")	첫 위치(정수)	ValueError 에러	위치가 필요하고 반드시 있다고 확신할 때
# "a" in s	True/False	False	위치는 필요 없고 있는지 여부만 볼 때

# "포함하는가"보다 더 정교한 검색 — 예를 들어 "숫자 3자리-4자리 형태의 전화번호"처럼 패턴으로 찾고 싶다면 정규표현식(regex)이 필요합니다. 이 장의 검색·판별 메서드를 한 단계 확장한 것으로, 14장에서 본격적으로 다룹니다.
