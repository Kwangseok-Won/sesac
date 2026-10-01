print({key: key ** 2 for key in range(1, 6)})

dedup = {ch for ch in "banana"} # set이라서 순서를 보장하지 않는다
print(dedup)
