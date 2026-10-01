# https://pilab-textbook.fly.dev/#/python/ch09_advanced_fn

scores = [
    {"name": "철수", "score": 85},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 58},
    {"name": "지영", "score": 73},
]

passed = [student["name"] for student in scores if student["score"] >= 60]
print(f"합격: {passed}")

ranking = sorted(scores, key=lambda student: student["score"], reverse=True)
for rank, student in enumerate(iterable=ranking, start=1): # enumerate(ranking, 1)는 1부터 번호를 매기며 순회
    print(f"{rank}등: {student['name']} ({student['score']}점)")

average = sum(student["score"] for student in scores) / len(scores)
print(f"평균: {average}")
