# args contains tuple if you give list and dictionary it will typecast in tuple automatically
# kwargs contains only dictionary if you give list and tuple it will give error
# kwargs dictionary contains only string key if you give numbers it will give error
# default arguments are not properly works with args and kwargs

def name(normal, *args, **kwargs):
    print(normal)
    for a in args:
        print(a)
    print("\nkwargs is started from here")
    for key, value in kwargs.items():
        print(f"{key} is {value}")


n = ['Nitin', 'Shayna']
roll = {"Nitin": "student", "Shayna": "student"}
normal = 'this is normal'
name(normal, *n, **roll)


def add(a, b=1, *args, **kwargs):
    print(args)
    print(kwargs)
    return a+b


print(add(3))
print(add(3, 2))
# l = [12, 11, 13]
# d = {'Nitin': 3}
# print(add(1, 3, *l, **d))
