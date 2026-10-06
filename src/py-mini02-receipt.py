# 주문 시스템에서 넘어온 값 (건드리지 마세요)
item = "아메리카노"
price_text = "4500"
qty_text = "2"

# 1단계 — 한 품목의 금액
line_total = int(price_text) * int(qty_text)

# 2단계 — 영수증 한 줄 (품목 왼쪽 10칸, 금액 오른쪽 8칸)
line = f"{item:<10}{line_total:>8}"

# 3단계 — 부가세(10%, 정수)와 합계
# vat = int(line_total * 0.1)
vat = line_total // 10
total = line_total + vat

print("-" * 20)
print(line)
print(f"{'부가세':<11}{vat:>8}")
print("-" * 20)
print(f"{'합계':<12}{total:>8}")
