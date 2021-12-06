class A:
 n = 0
 def __init__(self):
  self.k = 0
 def f(self):
  A.n += 1
  self.k += 1
A().f()
a = A()
a.f()
b = a
b.f()
print(a.n + b.k)
