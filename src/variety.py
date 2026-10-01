print([x for x in range(10)])

words = ["apple", "banana", "cherry"]

print([w.upper() for w in words])
upper_cased = []
for word in words:
    upper_cased.append(word.upper())
print("upper_cased: ", upper_cased)

print([len(w) for w in words])
length_in_words = []
for word in words:
    length_in_words.append(len(word))
print("length_in_words: ", length_in_words)

