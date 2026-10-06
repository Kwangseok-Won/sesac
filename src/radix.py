# 접두사로 진법 지정 → 전부 10진수로 해석됨
print(0b1010)   # 2진수 1010 → 10
print(0o17)     # 8진수 17 → 15
print(0xFF)     # 16진수 FF → 255

# 10진수를 다른 진법 문자열로 변환
print(bin(10))   # '0b1010'
print(hex(255))  # '0xff'
print(oct(15))   # '0o17'
