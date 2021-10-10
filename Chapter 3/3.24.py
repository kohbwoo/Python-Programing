num = int(input("숫자를 입력하세요 : "))
sum = 0

for i in range(1,num):
    sum = sum + (1/(i*i))

print("결과는",sum,"입니다.")