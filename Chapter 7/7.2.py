import time
stattime = time.time()

def sum1to10000000():
    return int(10000000*(10000000+1)/2)

sum1to10000000()
print("1에서 10000000까지의 합을 구하는 시간: ", round(time.time() - stattime, 5), "초")

stattime = time.time()
for i in range(100):
    sum1to10000000()
print("10000000까지의 합을 100번 반복해서 구하는 시간: ", round(time.time() - stattime, 5), "초")