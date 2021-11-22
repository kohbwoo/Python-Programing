def average(arg):#average function & exception
    try:
        return sum(arg) / len(arg)
    except ZeroDivisionError:
        raise Exception('empty argument')
    except:
        raise Exception('bad argument')
def test_average(arg):
    try:
        print(arg, ': ', end='')
        print(average(arg))
    except Exception as e:
        print(e)

test_average([1, 2, 3])
test_average([])
test_average(["가", "나"])