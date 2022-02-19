a = 100     # 정수형
b = -3.45   # 실수형
c = 5.36E10     # 소수점 표현
d = 0o153   # 8진수
e = 0x61    # 16진수

print(a)
print(b)
print(c)
print(d)
print(e)
print('\n'*3)

print(f"{a + b}\n"
      f"{b - c}\n"
      f"{c * d}\n"
      f"{d / e}\n"
      f"{a ** b}\n"
      f"{c % a}\n"
      f"{c // a}\n")
