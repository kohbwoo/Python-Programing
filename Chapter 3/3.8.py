x,y = input('점의 좌표 x, y를 입력하시오 : ').split()
x, y = int(x), int(y)
print(x,y)

if 0 <= x:
    if 0 <= y:
        print("1사분면에 있음")
    else:
        print("4사분면에 있음")
else:
    if 0 <= y:
        print("2사분면에 있음")
    else:
        print("3사분면에 있음")
