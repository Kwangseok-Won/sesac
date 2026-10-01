# raw 가 주어집니다. 직접 시험해보려면 아래 줄의 # 을 지우세요.
raw = "  Hong.GilDong@Example.COM  "

# 1단계 — 앞뒤 공백 없애고 소문자로
cleaned = raw.strip().lower()

# 2단계 — @ 앞뒤로 나누기
user = cleaned.split("@")[0]
domain = cleaned.split("@")[1]

# 3단계 — 보고 문자열
report = user + " / " + domain

print(report)
