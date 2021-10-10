num = int(input("숫자를 입력하세요 : "))
check = True
for i in range(2, num):
    if num % i == 0:
        check = False
        break

if check:
    print(num, "는 소수 입니다.")

else:
    print(num, "는 소수가 아닙니다.")