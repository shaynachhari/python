# class S:
#     #_a = '9'
#
#     def __init__(self):
#         self.__a = '9'
#         print(self.__a)
#         pass
#     pass
#
#
# class S1:
#     pass
#
# obj1 = S()
# obj1.__a = 'shayna'
#
#

class A:
    var = '9'
    pass

class B(A):
    var = '10'
    pass

class C(A):
    #var = '11'
    pass

class D(B,C):
    #var = '12'
    pass



d = D()
print(d.var)
#
# obj2 = S1()
# print(obj1._S__a)
# print(obj1.__dict__)
#
