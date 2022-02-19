aList = []
bList = [1, 2, 3]
cList = ['apple', 'banana', 'candy', 'dol']
dList = [10, 20, 'ever', 'friend']
eList = [33, 44, [555, 666]]

print(f"{aList} \n"
      f"{bList} \n"
      f"{cList} \n"
      f"{dList} \n"
      f"{eList} \n")

print(f"{cList[2]} \n"
      f"{eList[2]} \n"
      f"{dList[-1]} \n"
      f"{eList[2][0]} \n"
      f"{bList[:-1]} \n"
      f"{cList[1:]} \n"
      f"{dList[:]} \n")

print(bList + cList)
print(eList * 10)
print(len(eList))
fList = eList * 10
print(fList)
print(len(fList))

# [수정과 삭제]
fList[-1] = 10000
print(fList)
del fList[15:-1]
print(fList)

# [리스트 함수]
# append()  : 맨 뒤에 요소 추가
# sort()    : 순서 정렬
# reverse() : 그대로 뒤집기
# index()   : 위치 반환
# insert()  : a번째 위치 <- b 삽입
# remove()  : 첫번째 () 삭제
# pop()     : 반환 후, 삭제
# count()   : ()의 개수
# extend()  : 리스트 + 리스트
