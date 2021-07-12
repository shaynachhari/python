# Diamond shape problem is a confusion which occurs when we use multiple inheritance
class A:
    var = 9
    pass


class B(A):
    # var = 10
    pass


class C(A):
    # var = 11
    pass


class D(B, C):
    # var = 12
    pass


d = D()
print(d.var)
