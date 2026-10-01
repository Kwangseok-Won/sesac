scores = {"철수": 90, "영희": 85, "민수": 70}

for name, score in scores.items():
    print(f"{name}: {score}점")


for idx, value in enumerate(scores):
    print(idx, value)