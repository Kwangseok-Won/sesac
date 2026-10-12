from datetime import date, datetime

now = datetime.now()  # 현재 날짜·시간
print(now)
print(now.year, now.month, now.day)  # 연·월·일

# 날짜 계산: D-day
today = date.today()
exam = date(2026, 12, 25)
diff = exam - today  # 날짜끼리 빼기
print(f"시험까지 {diff.days}일")
