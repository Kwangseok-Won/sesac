fruit = "바나나"
menu = ["사과", "바나나", "포도"]
price = {"사과": 1000, "바나나": 2000, "포도": 5000}

if fruit in menu:
    print(f"{fruit}은(는) 메뉴에 있어요. 가격은 {price[fruit]}")

fruit = "자두"
if fruit not in menu:
    print(f"{fruit}은(는) 메뉴에 없어요.")

age = 25
if age >= 20 and age < 30:
    print("20대 입니다")

if 20 <= age < 30:
    print("20대 입니다 (chained comparison)")

print("*" * 50)

fruit = input("찾을 과일 입력: ")
if fruit in menu:
    print(f"{fruit}은(는) 메뉴에 있어요. 가격은 {price[fruit]}")
else:
    print(f"{fruit}은(는) 메뉴에 없어요")
