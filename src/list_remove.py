nums = [10, 20, 30, 20]

nums.remove(20) # 값 20을 앞에서 하나 삭제
print(nums) # [10, 30, 20]

last = nums.pop() # 맨 뒤 요소를 꺼내며 삭제
print(last, nums) # 20 [10, 30]

del nums[0]
print(nums)
