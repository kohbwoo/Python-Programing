def max2(m, n):
    if n > m:
        return n
    else:
        return m


def min2(m, n):
    if n > m:
        return m
    else:
        return n


print("100과 200중 큰 수는 :", max2(100, 200))
print("100과 200중 작은 수는 :", min2(100, 200))
