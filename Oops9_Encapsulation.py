# Encapsulation is a object oriented programming concept.
# It describes the idea of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data
# we use private and protected access specifier for achieving Encapsulation

"""
Access specifiers are used to imposing restrictions on directly accessing variables and methods.
There are three types of Access specifiers(modifiers).
1- Public
2- protected --> (_)
3- private --> (__)
"""


class Base:
    # _a = "9"

    def __init__(self):
        self.__a = "9"
        print(self.__a)
        pass
    pass


class Derived(Base):
    def __init__(self):
        # print(self._a)
        pass
    pass


obj1 = Base()
# obj1._a = "Nitin"

# obj2 = Derived()
# print(obj1._Base__a)

# print(obj1._Base__a)  # ---> this is name mangling
# note--> We can use private member by python name mangling
print(obj1._Base__a)
