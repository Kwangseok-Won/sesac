# https://pilab-textbook.fly.dev/#/python/ch04b_string

# 흔한 실수 — join을 거꾸로 씀
#
# join은 구분자가 앞에 옵니다. parts.join("-")가 아니라 "-".join(parts)예요. "무엇으로 이어붙일지"를 먼저 쓴다고 기억하세요.

s = "abc,def,ghi"

# split → 가공 → join 패턴
print(",".join("a,b,c".split(",")))  # a,b,c
print(",".join(["a","b","c"]))
