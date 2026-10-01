# map·filter (참고)
#
# map(모든 요소 변형)과 filter(조건으로 거르기)도 람다와 함께 쓰지만, 사실 컴프리헨션으로 다 표현됩니다. 비교해 보세요.

nums = [1, 2, 3, 4, 5]

# map
print(list(map(lambda num: num ** 2, nums)))
print([num ** 2 for num in nums])

print("-" * 40)

# filter
print(list(filter(lambda num: num % 2 == 0, nums)))
print([num for num in nums if num % 2 == 0])

print("-" * 40)

print(map(lambda num: num ** 2, nums))
print(help(map))
