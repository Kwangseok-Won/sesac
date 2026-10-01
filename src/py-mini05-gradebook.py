# scores 가 주어집니다. 직접 시험해보려면 아래 줄의 # 을 지우세요.
scores = [95, 83, 71, 55]

grades: list[str] = []
counts = {"A": 0, "B": 0, "C": 0, "F": 0}
highest = scores[0]
lowest = scores[0]
total = 0

for score in scores:
    if score >= 90: grade = "A"
    if score >= 80: grade = "B"
    if score >= 70: grade = "C"
    else: grade = "F"

    grades.append(grade)
    counts[grade] += 1

    if highest < score:
        highest = score
    elif lowest > score:
        lowest = score

    total += score


# for count in zip(counts, grades):
#     print(count)


average = round(total / len(scores), 1)

for grade in ["A", "B", "C", "F"]:
    print(f"{grade}: {counts[grade]}")
