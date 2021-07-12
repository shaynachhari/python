a = 5  # -->globals


def func():
    a = 6
    print(a)
    a = 8
    print(a)

    def inside():
        global a
        a = 10
        print(a)
        return

    inside()
    print(a)
    return


func()


def count():
    print("i am 1st function")
    return


def subfun():
    print("I am 2nd function")
    count()
    return


subfun()



name = "None"
def hello():
    name = "shayna"
    def info():
        # name = "Nitin"
        global name
        name = "nitin"
        print(name)
    info()
    print(name)

hello()
print(name)