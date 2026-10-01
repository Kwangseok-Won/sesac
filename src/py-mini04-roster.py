from solution import sorted_scores

names = ["민수", "영희", "지우"]
scores = {"민수": 88, "영희": 72, "지우": 91}

names.append("철수")
scores["철수"] = 78
print(names, scores)

scores.update({"영희": 95})
print(scores)

average = sum(scores.values()) / len(scores)
print(f"average: {average}")

# sorted_scores = sorted(scores.values(), reverse=True)
top = max(scores.values())
print(f"top: {top}")

passed = []
for name, score in scores.items():
    if score >= 80:
        passed.append(name)

print(f"passed: {passed}")

passed = []
for name in names:
    if scores.get(name) >= 80:
        passed.append(name)

print(f"passed: {passed}")

# https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Comprehensions
passed = []
passed = [name for name, score in scores.items() if score >= 80]
print(f"passed: {passed}")
