x, y = input('점의 좌표 x, y를 입력하시오. : ').split()
x, y = int(x), int(y)

if (((x-3)**2)+((y-4)**2))**(1/2) > 10:
    print("원 외부에 있음")

else:
    print("원 내부에 있음")
