def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

num = int(input("항 번호 입력: "))
print("a("+str(num)+") =", Fibonacci(num))