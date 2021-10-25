def aac(r):
    return 3.14 * r ** 2, 2 * 3.14 * r
while True:
    num = float(input("반지름을 입력하시오: "))
    if num < 0:
        break
    A, B = aac(num)
    print("넓이 :", A, "둘레 :", B)
print("프로그램을 종료합니다.")