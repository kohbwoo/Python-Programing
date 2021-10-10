ans = []


for i in range (100, 1000):
    if (((i//100)**3) + ((i %100//10)**3) + ((i % 10)**3)) == i:
        ans.append(i)


print("세 자리의 암스트롱 수 : ", end="")
for i in ans:
    print(i, end=" ")