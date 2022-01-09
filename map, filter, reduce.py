# lst = ["25", "5", "84", "73"]
# for i in range(0, 4):
#     lst[i] = int(lst[i])
# print(lst)
# print(lst[0] + 1)
#         OR
# -------------------MAP---------------------
# Map is used to apply a function in all elements of an iterable.
# In map 1st argument stands for function which have you wanted to apply.
# second argument is stand for iterable
lst = ["25", "5", "84", "73"]
a = list(map(int, lst))
print(a)

natural = list(range(0, 10))
print(natural)
square = list(map(lambda x: x * x, natural))
print(square)


def square(x):
    return x * x


def cube(x):
    return x * x * x


fun = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), fun))
    print(val)

# -----------------FILTER-----------------------
# filter gives elements from iterable but that values should give true boolean for applied function
# filter have two arguments 1st should be a function which has to be applied
# 2nd argument should be a iterable


def even(num1):
    return num1 % 2 == 0


integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = list(filter(even, integers))
print(check)


def greater_5(n):
    return n > 5


greater = list(filter(greater_5, integers))
print(greater)

# -------------------REDUCE---------------------
# In reduce 1st argument stands for function which have you wanted to apply.
# second argument is stand for iterable
# reduce is evaluate the whole iterable accordance to function which is applied
# first it took two elements from iterable and treated them as applied function's argument
# and their result again treated as 1st argument of applied function and for 2nd argument
# now new element is taken from iterable
# and this process is done until all elements from iterable should be evaluate
from functools import reduce

list2 = [1, 2, 3, 4, 5, 6]
num = reduce(lambda x, y: x + y, list2)
print(num)
