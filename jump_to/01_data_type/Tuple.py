t1 = ()
t2 = (1,)
t3 = (11, 22, 33)
t4 = 44, 55, 66
t5 = ('aaa', 'bbb', ('ccc', 'ddd'))

# 1. 인덱싱
# 2. 슬라이싱
print(t5[1])
print(t5[1:-1])
print(t5[0:-1])

# 3. 더하기
# 4. 곱하기
# 5. 길이 구하기
print(t3 + t4)
print(t2 * 50)
print(len(t2 * 50))

# 6. 값 추가
print(t5 + (1234567890,))
# print(t5+(1234567890)) #오류 발생
