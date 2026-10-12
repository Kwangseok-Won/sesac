# 파일이 없으면 — FileNotFoundError
# 읽기 모드("r")로 여는데 그 파일이 없으면 어떻게 될까요?
# 파이썬은 FileNotFoundError를 내며 프로그램을 멈춥니다.
# 오타 난 파일명, 아직 만들지 않은 파일 — 실전에서 아주 흔한 상황이에요.
# 이럴 때 13장에서 배울 try-except로 미리 대비합니다.

# try 안에서 에러가 나면 프로그램이 죽는 대신 except 블록으로 넘어갑니다.
# 덕분에 마지막 줄까지 무사히 실행되죠.
# 예외처리의 원리와 else·finally는 바로 다음 13장에서 제대로 배웁니다
# — 여기선 "파일엔 이런 대비가 필요하다"는 감만 잡으세요.


# 존재하지 않는 파일을 읽으려 하면?
try:
    with open("ghost.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("파일이 없어요! 경로를 확인하세요.")

print("프로그램이 멈추지 않고 계속됩니다")
