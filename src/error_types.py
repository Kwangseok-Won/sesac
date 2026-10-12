def safe_get(data: list[int], index: int):
    try:
        return data[index]
    except IndexError:
        return "범위를 벗어났어요"
    except TypeError:
        return "인덱스는 숫자여야 해요"


nums = [10, 20, 30]
print(safe_get(nums, 1))
print(safe_get(nums, 99))
print(safe_get(nums, "a"))
