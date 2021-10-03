num = int(input("정수를 입력하시오 : "))
if not num % 2:
    print(num,"는(은) 2으(로) 나누어집니다.")
else:
    print(num, "는(은) 2으(로) 나누어지지 않습니다.")

if not num % 3:
    print(num, "는(은) 3으(로) 나누어집니다.")
else:
    print(num, "는(은) 3으(로) 나누어지지 않습니다.")

if (not num % 2) and (not num % 3):
    print(num, "는(은) 2와(과) 3모두로 나누어집니다.")
else:
    print(num, "는(은) 2와(과) 3모두로 나누어지지 않습니다.")