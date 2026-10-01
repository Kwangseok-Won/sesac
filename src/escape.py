# https://pilab-textbook.fly.dev/#/python/ch04b_string

print("첫 줄\n둘째 줄")
print("이름\t나이")
print("따옴표 \" 넣기")
print("역슬래시 \\ 하나")

print("-" * 40)

# 파일 경로처럼 역슬래시가 많은 문자열은 따옴표 앞에 r을 붙인 raw 문자열로 쓰면 이스케이프를 무시해 편합니다.
print("C:\name\test")
print(r"C:\name\test")
