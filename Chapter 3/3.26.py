n = int(input("n을 입력하시오 : "))
output = []
for i in range(1,n+1):

    for j in range(0,n):
        if (i%2):
            print((output+j) * i,end=" ")
        else:
            print((output-j) * i,end=" ")
    print()