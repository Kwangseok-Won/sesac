# ② return이 없으면 자동으로 None을 반환합니다. print만 하는 함수의 반환값을 변수에 담으면 None이 들어갑니다.

def just_print(x: str) -> None:
    print(x) # 화면엔 "안녕"이 나오지만


value = just_print("안녕")
print(value) # value는 None
