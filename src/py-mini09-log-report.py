import re


def parse(line: str):
    """(날짜, 시각, 등급, 메시지) 튜플. 형식이 안 맞으면 None."""

    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) (\w+) (.+)"

    if bool(re.fullmatch(pattern, line)) is False:
        return None
    return re.match(pattern, line).groups()


def count_levels(lines: list[str]):
    """등급별 건수. 깨진 줄은 세지 않습니다."""

    count_by_level: dict[str, int] = {}
    for line in lines:
        parsed = parse(line)
        if parsed:
            _, time, _, _ = parsed


def busiest_hour(lines):
    """가장 많은 로그가 찍힌 시(두 자리 문자열). 없으면 None."""
    pass


LINES = [
    "2026-08-11 09:15 ERROR 결제 실패",
    "2026-08-11 09:16 INFO 사용자 로그인",
    "이건 로그가 아닙니다",
    "2026-08-11 09:20 ERROR DB 연결 끊김",
    "2026-08-11 14:31 WARN 응답 지연",
    "",
]
print(parse(LINES[0]))

print(count_levels(LINES))
