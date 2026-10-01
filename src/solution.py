scores: dict[str, int] = {"민수": 88, "영희": 72}

scores["영희"] = 95
print(scores)

scores.update({"철수": 78})
print(scores)

values = scores.values()
sorted_scores: list[int] = sorted(values, reverse=True)
# ranking = list(values)
# ranking.sort(reverse=True)
print(sorted_scores)
