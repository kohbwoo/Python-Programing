day = 0
m = 0
while True:
    day = day + 1
    m = m + 7
    print("day1 :", day, "달팽이의 위치 :", m, "미터")
    if m >= 30:
        break
    m = m - 5
print("우물을 탈출하는데 걸린 날은 ", day, "일 입니다.")
