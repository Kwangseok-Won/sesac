# 흔한 실수 — sort()는 아무것도 돌려주지 않는다
#
# result = nums.sort()라고 쓰면 result에는 None이 담깁니다!
# sort()는 원본 리스트를 직접 정렬하고 아무것도 반환하지 않아요.
# 원본을 그대로 두고 정렬된 새 리스트가 필요하면 sorted(nums)를 쓰세요.

nums = [3, 1, 4, 1, 5, 9, 2]

nums.sort()              # 오름차순 정렬(원본을 바꿈)
print(nums)              # [1,1,2,3,4,5,9]
nums.sort(reverse=True)  # 내림차순
print(nums)

print(sum(nums))         # 합계
print(max(nums), min(nums)) # 최대, 최소
print(nums.count(1))     # 1의 개수
print(nums.index(4))     # 4의 위치
