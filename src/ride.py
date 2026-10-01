height = int(input("키(cm): "))
age = int(input("나이: "))

if height >= 140 and age >= 12:
    print("탑승 가능합니다! 🎢")
elif height>= 140:
    print("키는 되지만 나이가 부족해요")
else:
    print("키 140cm 이상이어야 합니다")
