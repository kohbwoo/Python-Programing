num1, num2, num3 = input('세 복권번호를 입력하시오 : ').split()
num1, num2, num3 = int(num1), int(num2), int(num3)
key1, key2, key3 = 2, 3, 9
point = 0
if num1 == key1:
    point = point + 1
if num2 == key2:
    point = point + 1
if num3 == key3:
    point = point +1

if point == 0:
    print("다음 기회에...")
elif point == 1:
    print("상금 1만 원")
elif point == 2:
    print("상금 1천만 원")
elif point == 3:
    print("상금 1억원")