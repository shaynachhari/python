# object introspection means getting details of objects
# type returns object type
# id returns a unique id of every object
# dir returns a list of method and function that can be apply on the object
# we have inspect module to make such method that can return object info

var = "Shayna"
lst = ["Shayna", "Nitin", 24, 11]
tup = ("Kimmi", "Nik", 12, 10)
sett = {"Chhari", "Goswami", 2000, 2002}
dic = {"Nitin": "Shayna", "Goswami": "Chhari"}


class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
        pass

    def intro(self):
        return f"Student name is {self.name} for branch {self.branch}"
    pass


shayna = Student("Shayna Chhari", "CS")
nitin = Student("Nitin Goswami", "CS")

print(type(var))
print(type(lst))
print(type(tup))
print(type(sett))
print(type(dic))
print(type(shayna))
print(type(nitin))
print(type(shayna.intro))

print(id(var))
print(id(lst))
print(id(tup))
print(id(sett))
print(id(dic))
print(id(shayna))
print(id(nitin))
print(id(shayna.intro))
print(id("India"))
print(id("India1"))

print(dir(var))
print(dir(lst))
print(dir(tup))
print(dir(sett))
print(dir(dic))
print(dir(shayna))
print(dir(nitin))
print(dir(shayna.intro))
print(dir("India"))
print(dir("India1"))
