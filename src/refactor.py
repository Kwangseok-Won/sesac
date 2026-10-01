def print_dan(dan: float):
    print(f"--- {dan}단 ---")

    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")


print_dan(3)
print_dan(7)


def is_even(n):
    return n % 2 == 0


print(is_even(10))
print(is_even(7))
