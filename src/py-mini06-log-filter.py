LINES = [
    "2026-08-11 09:15 ERROR 결제 실패",
    "2026-08-11 09:16 INFO 사용자 로그인",
    "2026-08-11 09:20 ERROR DB 연결 끊김",
    "2026-08-11 09:31 WARN 응답 지연",
]


def errors(lines: list[str]) -> list[str]:
    """ERROR 가 들어간 줄만 골라 돌려줍니다."""
    print([line for line in lines if line.count("ERROR")])
    return [line for line in lines if line.count("ERROR")]
    return [line for line in lines if "ERROR" in line]

    has_error = []
    for line in lines:
        if line.count("ERROR"):
            has_error.append(line)
    return has_error


def messages(lines: list[str]) -> list[str]:
    """각 줄에서 메시지 부분만 골라 돌려줍니다."""
    message_list = []
    for line in lines:
        message_list.append(*line.split(" ", 3)[3:])

        # msg = " ".join(line.split()[3:])
        # message_list.append(msg)
    return message_list
    return [line.split(" ", 3)[3:] for line in lines]


def summary(lines: list[str]) -> list[str]:
    """ERROR 줄의 메시지만 모아 돌려줍니다. 위 두 함수를 이어 쓰세요."""

    summary_list = []
    for error in errors(lines):
        for message in messages(lines):
            if message in error:
                summary_list.append(message)

    return summary_list


print(summary(LINES))
