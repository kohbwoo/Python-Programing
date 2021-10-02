a, b = input('두 정수 입력: ').split()
a,b = int(a), int(b)
if a % b == 0:
    print(a, "는(은)", b, "의 배수입니다.")
else:
    print(a, "는(은)", b, "의 배수가 아닙니다.")
