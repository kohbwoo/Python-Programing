
for num in range(1,12+1):
    check = True
    for i in range(2, num):
        if num % i == 0:
            check = False
            break

    if check:
        print(num, "소수")

    else:
        print(num, "합성수")