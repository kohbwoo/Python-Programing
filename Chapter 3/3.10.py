a, b = input('두 정수 입력: ').split()
a,b = int(a), int(b)
if a%b == 0:
    print("{}는(은) {}의 배수입니다.".format(a,b))
else:
    print("{}는(은) {}의 배수가 아닙니다.".format(a, b))
