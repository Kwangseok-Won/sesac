# 중첩 반복(for 안의 for)으로 구구단

# 2단부터 4단까지
for dan in range(2, 5):
    print(f"--- {dan}단 ---")

    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
