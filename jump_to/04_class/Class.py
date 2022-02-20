class FirstClass:
    def firstFunction(a, b):
        print(f"{a + b} \n")
        return a + b

    a = 10
    b = 15
    # firstFunction(a, b)
    c = firstFunction(a, b)
    d = firstFunction(111, 222)

    print(a)
    print(b)
    print(c)
    print(d)

# if __name__ == '__main__':
#     print("메인 테스트")
