var = "Shayna"
lst = ["Shayna","Nitin",24 , 11]
tup = ("Kimmi","Nik",12,10)
dict = {"chhari":"Shayna"  , "Goswami":"Nitin"}
sett = {"shayna",8,0,"Nik"}


class Student:
    def __init__(self,name,branch):
        self.name = name
        self.branch= branch

    def intro(self):
        return f"Student is {self.name} for branch {}"

