def f(a):
 if a < 0:
  raise ValueError()
 else:
  raise Exception()

v = 0

try:
 f(-1)#기본
except Exception:
 v += 1
except ValueError:
 v += 2
else:
 v += 3
finally:
 v += 4#최종

# V = 0 + 1 + 4
print(v)#5