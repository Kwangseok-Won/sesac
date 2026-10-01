# https://pilab-textbook.fly.dev/#/python/ch04b_string

s = "xxHelloxx"
print(s.strip("x"))
print(s.lstrip("x"))
print(s.rstrip("x"))

t = "aaa"
print(t.replace("a", "b")) # 전부 → bbb
print(t.replace("a", "b", 2)) # 2개만 → bba

print("Hello World".swapcase())

print("hello world".title()) # 각 단어 첫 글자 대문자
print("hello world".capitalize()) # 문장 첫 글자만 대문자
