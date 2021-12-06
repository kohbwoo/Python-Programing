class A:
    def __init__(self):
        self.__a = 0
        self.__a__ = 0
    def f(self):
        print(self.__a) # (...)
        
#print(A().__a) # (...)실패

print(A().__a__) # (...)