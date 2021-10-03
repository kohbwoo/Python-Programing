def sum_avg(*args):
    return sum(args), sum(args) / len(args)


s, a = sum_avg(1.1, 2.2, 3.3, 4.4)