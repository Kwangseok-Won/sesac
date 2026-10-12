import random

while True:
    guess = input("주사위 눈 예상(1부터 6까지, q=종료): ")
    if guess.lower() == "q":
        print("게임 종료")
        break

    try:
        user_guess = int(guess)
    except ValueError:
        print("숫자를 입력하세요!")
        continue

    dice_number = random.randint(1, 6)
    print(f"주사위: {dice_number}")

    if user_guess == dice_number:
        print("정답! 🎲")
    else:
        print("아쉬워요")
