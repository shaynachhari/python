class Student:
    univercity = "RGPV"

    def __init__(self,name , roll):
        self.name = name
        self.roll = roll

    @staticmethod

    def details():
        print("Shiri ram group of engineering and managment")
    pass

shayna = Student("shayna",71)
print(shayna.name)
print(shayna.details())
shayna.details()
Student.details()


