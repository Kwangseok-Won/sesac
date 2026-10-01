numbers: list[int] = list(range(0, 50, 3))
print(f"numbers: {numbers}")

multiplier = int(input("원하는 배수: "))

odd = []; even = []; user_defined = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    if number % multiplier == 0:
        user_defined.append(number)
        if user_defined.count(0):
            user_defined.remove(0)

print(f"짝수: {even}")
print(f"홀수: {odd}")

print(f"{multiplier}의 배수: {user_defined}")
