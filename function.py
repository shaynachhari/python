def nitin(n, s):
    """using return and print"""  # this is docstring not a comment
    print("shayna")
    return n, "love", s


l = nitin("Nitin", "Shayna")
print(l)


def add(x, y):
    """using only return"""    # Docstring is used to recognising the work and mean of funtion
    return x+y


a = add(1, 2)
print(a)


def ns():
    """using only print"""
    print("love")
ns()
print(ns.__doc__)  # This is used to print docstring
print(nitin.__doc__)
print(add.__doc__)


def divide(x, y):
    print("the divide of the numbers is", end=':')
    return x/y


print(divide(8, 4))


def add(x,y):
    """using only return with add two numbers"""
    return x+y


print(add.__doc__)