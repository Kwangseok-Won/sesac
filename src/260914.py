a = 1 # 출력 결과 끝 부분에 'a': 1
print(globals())

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000024376AF0BB0>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\opt\\sesac\\exercise\\src\\260914.py', '__cached__': None, 'a': 1}

def main():
    print("hello world")

if __name__ == "__main__":
    main()