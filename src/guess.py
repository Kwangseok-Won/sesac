answer = 7 # 정답 (바꿔보세요)

while True:
    guess = int(input("1 - 10 중 맞혀보세요: "))

    if guess == answer:
        print("정답! 🎉")
        break
    elif guess < answer:
        print("더 큰 수예요")
    else:
        print("더 작은 수예요")
