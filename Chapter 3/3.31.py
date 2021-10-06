import time
stattime = time.time()
for x in range(1, 1501):
    for y in range(1, 1501):

        if x == y:
            continue

        sum1 = 0
        sum2 = 0

        for i in range(1, x):
            if (x % i) == 0:
                sum1 += i

        for j in range(1, y):
            if (y % j) == 0:
                sum2 += j

        if (sum1 == y) and (sum2 == x):
            print(x, "의 친화수", y)

print("Runtime :", round(time.time() - stattime, 3), "S")
