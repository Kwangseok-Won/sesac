def pick(names: list[str], length=3):
    """{length} 글자 이상인 이름만 골라 대문자로 바꿔 돌려줍니다."""

    # 반복문으로 구현
    upper_names = []
    for name in names:
        if len(name) >= length:
            upper_names.append(name.upper())
    # return upper_names

    return [
        name.upper() for name in names if len(name) >= length
    ]  # Comprehension으로 구현


name_list = [
    "John",
    "Peter",
    "Be",
    "Emily",
    "Alice",
    "Bob",
    "Charlie",
    "Doe",
    "Elton",
    "Frank",
    "Gibson",
    "Holt",
    "Iris",
    "Jill",
    "Kenneth",
    "Lincoln",
]

print(pick(name_list, length=5))
