class Employee:
    salary = 30000
    total_leaves = 10

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    @classmethod
    # this is class method decorator
    # this is used to change class variables
    def change_leaves(cls, new_leaves):
        cls.total_leaves = new_leaves

    def details(self):
        return f"{self.name} and their no. is {self.phone}"
    pass


shayna = Employee("Shayna Chhari", "6262834698")
# print(shayna.name)
print(shayna.details())
print(shayna.total_leaves)
shayna.change_leaves(50)
print(shayna.total_leaves)