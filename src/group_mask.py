import re

text = "제 번호는 010-1234-5678 입니다"

# () 그룹으로 부분 포착
m = re.search(r"(\d{3})-(\d{4})-(\d{4})", text)
print(m.group())  # 전체 → 010-1234-5678
print(m.group(1))  # 첫 그룹 → 010
print(m.group(2))  # 둘째 그룹 → 1234

# sub + 그룹 되살리기(\1, \2)로 가운데 마스킹
masked = re.sub(r"(\d{3})-\d{4}-(\d{4})", r"\1-****-\2", text)
print(masked)  # 제 번호는 010-****-5678 입니다
