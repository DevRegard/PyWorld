i = 10
while i >= 0:
    print(f"{i} \t {i**i}")
    i = i - 1

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 칩니다." % treeHit)
    if treeHit == 10:
        print("나무 죽다.")
