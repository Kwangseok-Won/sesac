# w: 새로 쓰기 (파일을 처음부터 비우고 시작)
f = open("log.txt", "w")
_ = f.write("첫 기록\n")
f.close()

# a: 이어 쓰기 (첫 기록은 그대로, 뒤에 덧붙임)
f = open("log.txt", "a")
_ = f.write("둘째 기록\n")
f.close()

f = open("log.txt", "r")
print(f.read())  # 첫 기록 / 둘째 기록 (둘 다 남아 있다)
f.close()
