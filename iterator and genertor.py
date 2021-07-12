"""
iterate -- the work which will going to happen
iterable -- the object in which these two methods are defined __iter__ or __getitem__
iterator -- on applying __iter__ method on iterable it returns iterator
iteration -- the process in which iterate is going on is called iteration.
generator -- it is type of iterator which generates value on the runtime.
__next__ -- iterate only one time
"""
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(9):
#     print(i)
# making iterator
a = lst.__iter__()
print(a)


# making generator
def gen(a):
    for i in range(a):
        yield i


for i in gen(10):
    print(i)

lst01 = gen(15)
print(gen(9))

tup = (5, 6, 8, 22, 9, 55, 33)
b = tup.__iter__()
print(b)
print(b.__next__())
print(b.__next__())


# for i in b:
#     if i == 22:
#         print(i)


def shayna(nitin):
    for i in range(nitin + 1):
        yield i


for i in shayna(10):
    print(i)

a = shayna(5)
print(a.__next__())
print(a.__next__())
