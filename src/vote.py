votes = ["철수", "영희", "철수", "민수", "철수", "영희"]

candidates = set(votes)
print("후보: ", candidates)

count = {}
for vote in votes:
    count[vote] = count.get(vote, 0) + 1
print("집계: ", count)

winner = max(count, key=count.get)
print(f"당선: {winner}")
