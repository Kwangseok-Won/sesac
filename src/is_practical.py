# https://pilab-textbook.fly.dev/#/python/ch04b_string

user = input("나이를 입력: ")
if user.isdigit():
    print("내년엔", int(user) + 1, "살")
else:
    print("숫자를 입력해 주세요!")
