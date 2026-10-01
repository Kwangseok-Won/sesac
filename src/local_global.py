a = 100

def show() -> None:
    a = 1 # 함수 안에서 전역변수를 바꾸려면 global 키워드가 필요하지만, 되도록 안 쓰는 게 좋습니다
    print(f"함수 안 a: {a}")


show()
print(f"함수 밖 a: {a}")
