logged_in = True
is_admin = False

if logged_in:
    print("환영합니다!")

    if is_admin:
        print("관리자 메뉴를 표시합니다")
    else:
        print("일반 사용자 화면입니다")

else:
    print("로그인이 필요합니다")

###

if logged_in and is_admin:
    print("환영합니다!")
    print("관리자 메뉴를 표시합니다")
elif logged_in and not is_admin:
    print("환영합니다!")
    print("일반 사용자 화면입니다")
else:
    print("로그인이 필요합니다")
