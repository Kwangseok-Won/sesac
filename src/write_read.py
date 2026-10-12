# ① 쓰기 모드로 열어서 파일에 쓴다
f = open("memo", "w", encoding="utf-8")
_ = f.write("첫 줄입니다\n")
_ = f.write("둘째 줄입니다\n")
f.close()  # flush

# ① 읽기 모드로 다시 열어서 내용을 읽는다
f = open("memo", "r", encoding="utf-8")
content = f.read()
f.close()

print(content)
