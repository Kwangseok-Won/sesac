def my_func():
    x = 10
    print(f"함수 안: {x}")


my_func()
# 마지막 줄에서 에러가 납니다 — x는 함수가 끝나면 사라지니까요. 이게 오히려 장점입니다.
# 함수마다 변수가 격리돼서, 다른 함수의 변수와 이름이 겹쳐도 안전해요.
# print(x) # NameError: name 'x' is not defined
