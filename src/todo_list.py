# 맨 앞의 open("todo.txt", "w").close()는 파일을 깨끗이 비우는 관용구입니다
# — 이게 없으면 실행할 때마다 a가 계속 쌓여 항목이 중복돼요.
# with로 안전하게 열고, for line in f로 순회하고, strip()으로 줄바꿈을 정리한 — 이번 장 전체가 담긴 실전 코드입니다.

# 가장 아픈 실수 — w 모드는 기존 내용을 통째로 지운다
# open("소중한파일.txt", "w") — 이 한 줄로 파일 안의 모든 내용이 사라집니다.
# 아직 아무것도 쓰지 않았어도, 여는 순간 이미 비워져요.
# 이어 붙이려던 것이었다면 "w"가 아니라 "a"였어야 합니다.
# 실수로 소중한 파일을 날리는 1순위 사고이니,
# 쓰기 전에는 늘 "이 파일을 비워도 되나, 이어 써야 하나?"를 한 번 생각하세요.


memos = ["우유 사기", "운동 30분", "책 읽기"]

open("todo", "w", encoding="utf-8").close()  # 먼저 빈 파일로 초기화

# 항목을 하나씩 이어 쓰기 (a 모드)
for memo in memos:
    with open("todo", "a", encoding="utf-8") as f:
        _ = f.write(memo + "\n")

# 번호를 매겨 다시 읽기
num = 1
with open("todo", "r", encoding="utf-8") as f:
    for line in f:
        print(f"{num}. {line.strip()}")  # strip으로 줄바꿈 제거
        num += 1
