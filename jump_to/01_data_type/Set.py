s1 = set([10, 20, 30])
s2 = set("안녕 하세요")

print(s1)
print(s2)

# [자료형 변환]
listS1 = list(s1)
listS2 = list(s2)

print(listS1)
print(listS2)

tupleL1 = tuple(listS1)
tupleL2 = tuple(listS2)

print(tupleL1)
print(tupleL2)

# [교집합, 합집합, 차집합]
ss1 = set([11, 22, 33, 44, 55, 66])
ss2 = set([44, 55, 66, 77, 88, 99])

print(f"\n{ss1 & ss2} \n"
      f"{ss1.intersection(ss2)} \n"
      f"{ss1 | ss2} \n"
      f"{ss1.union(ss2)} \n"
      f"{ss2 - ss1} \n"
      f"{ss1.difference(ss2)} \n")

# [집합 함수]
# add()     : 1개만 추가
# update()  : 한번에 추가
# remove()  : 특정값 삭제
