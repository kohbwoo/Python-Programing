n = int(input("n을 입력하시오 : "))
num_List = [[0] * n for _ in range(n)]
num = 1
for i in range(0, n):
    for j in range(0, n):
        num_List[i][j] = num
        num = num + 1

for i in range(0, n):
    if i % 2 == 1:
        num_List[i].sort(reverse=True)
    for j in range(0, n):
        print(num_List[i][j], end="\t")
    print()
