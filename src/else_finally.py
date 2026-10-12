# https://pilab-textbook.fly.dev/#/python/ch13_stdlib

# else와 finally
# try에는 else와 finally를 더할 수 있습니다. 흐름을 기억하세요
# — "일단 try, 실패하면 except, 성공하면 else, 어쨌든 finally".

# else는 에러가 안 났을 때만 실행됩니다.


def divide(a: int, b: int):
    try:
        result = a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없어요")
    else:
        print(f"결과: {result}")  # 성공했을 때만
    finally:
        print("계산 완료")  # 항상 실행


divide(10, 2)  # 결과: 5.0 → 계산 완료
print("---")
divide(10, 0)  # 0으로 나눌 수 없어요 → 계산 완료
