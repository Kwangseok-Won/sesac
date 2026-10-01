# https://pilab-textbook.fly.dev/#/python/ch05_mutable

nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)

s = {1, 2, 3}
s.add(4)
s.update([5, 6]) # 여러 개 추가
s.remove(1)
print(s)
