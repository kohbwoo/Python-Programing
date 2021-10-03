num = int(input("1에서 9까지의 수를 입력하시오. :"))
while 0>= num or num >= 10:
    num = int(input("1에서 9까지의 수를 다시 입력하시오. :"))


print("for")
for i in range(1,10):
    print(num, "*",i,"=",num*i)

print("while")
i = 1
while(i < 10):
    print(num, "*", i, "=", num * i)
    i += 1