# 요즘은 경로를 문자열로 다루는 대신 pathlib의 Path를 많이 씁니다. 운영체제(/ vs \) 차이를 알아서 처리해 주고, 읽기·쓰기도 한 줄로 끝나요.

from pathlib import Path

# open/write/close 없이 한 줄로 쓰고 읽기
_ = Path("note.txt").write_text("pathlib은 한 줄이면 된다\n")
text = Path("note.txt").read_text()
print(text)  # pathlib은 한 줄이면 된다
