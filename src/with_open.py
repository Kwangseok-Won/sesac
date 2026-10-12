# with 블록이 끝나면 파일이 자동으로 닫힌다 — close() 불필요
with open("hello.txt", "w") as f:
    _ = f.write("with는 편하고 안전하다\n")
# 여기서 f는 이미 닫힌 상태

with open("hello.txt", "r") as f:
    print(f.read())  # with는 편하고 안전하다
