cal = int(input("1)덧셈\t2)뺄셈\t3)곱셈\t4)나눗셈\n\r어떤 연산을 원하는지 번호를 입력하세요.: "))
num1 = int(input("연산을 원하는 숫자 두개를 입력하세요\n"))
num2 = int(input())
if cal == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif cal == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif cal == 3:
    print(num1, "*", num2, "=", num1 * num2)
elif cal == 4:
    print(num1, "/", num2, "=", num1 / num2)
