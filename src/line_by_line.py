# 줄 단위로 처리하기
# 파일은 대개 여러 줄로 되어 있습니다. 7장에서 배운 for 반복문이 여기서 다시 등장해요
# — for line in f:라고 쓰면 파일을 한 줄씩 꺼내 반복합니다. 리스트를 순회하던 그 감각 그대로예요.

# 각 line은 "90\n"처럼 줄바꿈까지 포함한 문자열입니다.
# 다행히 int()는 앞뒤 공백·줄바꿈을 무시하므로 바로 숫자로 바꿀 수 있어요.
# 글자 그대로 다뤄야 할 땐 3장의 line.strip()으로 줄바꿈을 떼면 됩니다.

# 점수 세 줄을 파일로 저장
with open("scores", "w", encoding="utf-8") as f:
    _ = f.write("90\n85\n100\n")

# 한 줄씩 읽어 합계 구하기 (7장 for)
total = 0
with open("scores", "r") as f:
    for line in f:
        total += int(line)  # int()는 줄바꿈을 알아서 무시


print("합계: ", total)  # 90+85+100 = 275
