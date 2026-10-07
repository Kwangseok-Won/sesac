a = 100


def show() -> None:
    # global a  # 함수 안에서 전역변수를 바꾸려면 global 키워드가 필요하지만, 되도록 안 쓰는 게 좋습니다
    a = 1
    print(f"함수 안 a: {a}")


show()
print(f"함수 밖 a: {a}")
