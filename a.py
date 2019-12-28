from sympy.core.singleton import Singleton


@Singleton
class A(object):
    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)

print(id(a1), id(a2))