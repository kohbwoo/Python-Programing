def mean6(a, b, c, d, e, f):
    tmp = [a, b, c, d, e, f]
    return sum(tmp)/6


def max6(a, b, c, d, e, f):
    return max(a, b, c, d, e, f)


def min6(a, b, c, d, e, f):
    return min(a, b, c, d, e, f)


a, b, c, d, e, f = input('여섯 개의 수를 입력하시오. : ').split()
a, b, c, d, e, f = int(a), int(b), int(c), int(d), int(e), int(f)
print(a, b, c, d, e, f, "의 평균값은", mean6(a, b, c, d, e, f))
print(a, b, c, d, e, f, "의 최대값은", max6(a, b, c, d, e, f))
print(a, b, c, d, e, f, "의 최소값은", min6(a, b, c, d, e, f))
