import re

print(re.findall(r"\d+", "abc123"))  # raw → 정상 → ['123']

# r"\d"는 백슬래시+d 두 글자, "\\d"와 똑같다
print("\\d" == r"\d")  # True
