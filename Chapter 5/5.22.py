n = int(input("n을 입력하시오 : "))
num_List = [0 * n for _ in range(n*n)]
num = 1
for i in range(1, n*n+1):
    num_List[i-1] = i

for i in range(0, (len(num_List)+n)-1, n):
    if i % 10 == 0:
        for j in num_List[i:i+n]:
            print(j, end= "\t")

    else:
        for j in sorted(num_List[i:i+n], reverse=True):
            print(j, end= "\t")
    print()

