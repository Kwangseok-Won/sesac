# 주의 — 맨몸 except는 피하기
# except:만 쓰면 모든 에러를 뭉뚱그려 잡아, 진짜 문제(오타 등)까지 숨겨버립니다.
# except ValueError:처럼 어떤 에러를 잡을지 지정하는 게 좋습니다.


# 에러 없이 끝나는 코드 (try만)
try:
    num = int(input("숫자를 입력: "))
    print(f"제곱은 {num**2}")
except:
    print("숫자가 아니에요! 다시 시도하세요.")
    raise

print("프로그램은 계속됩니다")  # 에러가 나도 여기 도달
