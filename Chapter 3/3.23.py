input = int(input("숫자를 입력하세요 :"))
output = 0
for i in range(0, input+1):
    output += i ** 2
print(output)