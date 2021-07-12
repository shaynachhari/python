class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@gmail.com"
        pass

    def explain(self):
        return f"This student is {self.fname} {self.lname}"

    # property decorator is used for using a method as an attribute(variable)
    @property
    def email(self):
        if self.fname is None and self.lname is None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"

    # setter is used to set attribute value
    @email.setter
    def email(self, mail):
        name = mail.split("@")[0]
        first, last = name.split(".")
        self.fname, self.lname = first, last
        pass

    # deleter is used to delete attribute value when we use del statement
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
        pass

    pass


shayna = Student("Shayna", "Chhari")
print(shayna.email)
# shayna.email
shayna.lname = "Goswami"
print(shayna.email)
shayna.email = "nitin.goswami@gmail.com"
print(shayna.email)
print(shayna.fname)
print(shayna.lname)

del shayna.email

print(shayna.email)
shayna.email = "Shayna.Chhari@gmail.com"
print(shayna.email)
print(shayna.fname)
print(shayna.lname)
