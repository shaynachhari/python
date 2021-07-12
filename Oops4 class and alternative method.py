class Employee:
    salary = 30000
    total_leaves = 10

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.total_leaves = new_leaves

    @classmethod
    # we can use class method as alternate constructor
    def one(cls, string):
        return cls(*string.split("-"))

    def details(self):
        return f"{self.name} and their no. is {self.phone}"
    pass


shayna = Employee.one("Shayna-6262834698")
print(shayna.phone)

nitin = Employee.one("Nitin goswami-7999676443")
print(nitin.details())
