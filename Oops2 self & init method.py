class Students:
    name = "name"
    roll = 0
    cgpa = 0.0

    def __init__(self, stu_name, stu_roll):
        # init is a constructor method in python
        # constructor is a special type of method which is used to initialize the instance members of the class
        # type of constructor
        # 1 - default constructor
        # 2 -parameterized constructor
        # The constructor is a method that is called when an object is created
        # If you create four objects, the class constructor is called four times.
        self.name = stu_name
        self.roll = stu_roll
        pass

    def print_details(self):  # The functions in classes is called Methods
        # self is parameter use for getting object as a argument.
        # self is used in every method which we want to make
        return f"The Name is {self.name}.\nRoll no. is {self.roll}.\nCGPA is {self.cgpa}"
    pass


nitin = Students("Nitin goswami", "71")
shayna = Students("Shayna chhari", "51")
# nitin.name = "Nitin"
# nitin.roll = "0904cs191051"
# nitin.cgpa = "9.1"
#
# shayna.name = "Shayna"
# shayna.roll = "0904cs191071"

print(shayna.print_details())
print(nitin.print_details())