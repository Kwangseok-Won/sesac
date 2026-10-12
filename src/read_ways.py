# read · readlines — 통째로 vs 리스트로
# 파일을 읽는 방법은 여럿입니다. 상황에 맞게 고르세요.

# 언제 무엇을?
# — read()는 "내용 전체가 필요할 때"(짧은 파일),
# readlines()는 "줄 목록을 리스트로 다루고 싶을 때",
# for line in f는 "한 줄씩 처리만 하면 될 때".
# 셋 중 큰 파일에는 for line in f가 가장 안전해요 — 한 줄씩만 메모리에 올리니까요.

with open("scores.txt", "w") as f:
    _ = f.write("90\n85\n100\n")

# read(): 전체를 하나의 문자열로
with open("scores.txt", "r") as f:
    print(repr(f.read()))  # '90\n85\n100\n'

# readlines(): 줄들을 리스트로
with open("scores.txt", "r") as f:
    lines = f.readlines()
print(lines)  # ['90\n', '85\n', '100\n']
print(len(lines), "줄")  # 3 줄
