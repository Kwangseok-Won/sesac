# for-else — 끝까지 돌았는지 확인
# for에도 else를 붙일 수 있습니다. if의 else와 헷갈리기 쉬운데, 뜻이 달라요
# — "for가 break로 끊기지 않고 끝까지 돌았을 때만" else가 실행됩니다. "다 찾아봤는데 없었다"를 표현할 때 유용해요.
#
# data에 11을 추가하면 break가 걸려 else가 실행되지 않습니다. 직접 바꿔 실행해 보세요.
# else의 들여쓰기는 for와 같은 높이라는 점도 눈여겨보세요.

data = [2, 4, 6, 8]

# 10보다 큰 수를 찾아본다
for n in data:
    if n > 10:
        print(f"찾음: {n}")
        break
else:
    print("10보다 큰 수가 없습니다")
