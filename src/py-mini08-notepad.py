def add(path: str, memo: str):
    """메모 한 줄을 파일 뒤에 덧붙입니다."""
    with open(path, "a", encoding="utf-8") as f:
        _ = f.write(memo + "\n")


def read_all(path: str) -> list[str] | None:
    """모든 메모를 리스트로. 파일이 없으면 빈 리스트."""
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                return [line.strip()]
    except FileNotFoundError:
        return []


def find(path: str, word: str) -> list[str]:
    """그 단어가 들어간 메모만 골라 돌려줍니다."""
    memos = read_all(path)
    return [memo for memo in memos if word in memo]


def clear(path: str):
    """메모를 전부 지웁니다."""
    with open(path, "w") as f:
        _ = f.write("")
    # open(path, "w", encoding="utf-8").close()


PATH = "memo.txt"

clear(PATH)

add(PATH, "우유 사기")
add(PATH, "책 반납")
print(read_all(PATH))


# for memo in ["우유 사기", "책 반납", "우유 데우기"]:
#     add(PATH, memo)
# print(find(PATH, "우유"))
