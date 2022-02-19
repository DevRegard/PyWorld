# ""
# ''
# """ """
# ''' '''

# \n
# \t
# \\
# \'
# \"
# \r
# \f
# \a
# \b
# \000

print("=" * 500)
a = "Regard"
b = " 50 "
print((a+b) * 50)
print("=" * 500)


# [슬라이싱]
print(
    f"{a[1]} \n"
    f"{a[-1]} \n"
    f"{a[4]} \n"
)


# [인덱싱]
print(
    f"{a[1:4]} \n"
    f"{a[2:-1]} \n"
    f"{a[2:]} \n"
    f"{a[:]} \n"
)


# [포매팅]
# 포맷 코드
print("today: %d / %d " % (2, 19))
print("I code in %s" % "Python")
print("Most important word : %s" % a)

#   %s
#   %c
#   %d
#   %f
#   %o
#   %x
#   %%

print("|%10s|" %a)
print("|%-10s| \n" %a)
pi = 3.14159265358979323846264338327
print("|%0.4f|" %pi)
print("|%-10.4f|" %pi)
print("|%10.4f| \n" %pi)

# format()
print("나는 오늘 {0}를 하고, {1}을 하는 중이다.".format("자바", "파이썬"))
print("오늘은 {month}월 {day}일이고, 현재 시간은 {hour}시 {minute}분이다. \n".format(month=2, day=19, hour=9, minute=37))

print("|{0:<10}|".format(a))
print("|{0:>10}|".format(a))
print("|{0:^10}|".format(a))
print("|{0:★^10}| \n".format(a))

print("|{0:0.4f}|".format(pi))
print("|{0:10.4f}| \n".format(pi))
print("|{0:10.4f}| \n".format(pi))


# f
d = {'nation':'KOREA', 'region':'Incheon'}
print(f"국적은 {d['nation']}이다. \n{d['region']}에 산다.\n")

print(f"{'|HELLO, HELLO, HELLO|':=^100}")
print(f"{'|HELLO, HELLO, HELLO|':!<100}\n")

print(f'{pi:0.5f}')
print(f'{pi:10.5f}')

# [문자열 함수]

# count()
# find()    : 없으면 -1 반환
# index()   : 없으면 오류
# join()    : "[삽입 문자]".join('[문자열, 리스트, 튜플]')      {삽입}

# upper()
# lower()

# lstrip()
# rstrip()
# strip()

# replace()
# split()   : [변수].split('[기준 문자]')                     {나누기}
