def mean3(a, b, c):
    return (a + b + c) / 3


def max3(a, b, c):
    return max(a, b, c)


def min3(a, b, c):
    return min(a, b, c)


a, b, c = input('세 수를 입력하시오. : ').split()
a, b, c = int(a), int(b), int(c)
print(a, b, c, "의 평균값은", mean3(a, b, c))
print(a, b, c, "의 최대값은", max3(a, b, c))
print(a, b, c, "의 최소값은", min3(a, b, c))
