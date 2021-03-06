# In operator overloading, one operator can be used for multiple functions
# eg--> "+" is used to add two integers as well as we can use it for combining two strings
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        pass

    def details(self):
        print(f"Student name is {self.name} and marks is {self.marks}")

    # Dunder method
    def __add__(self, other):
        return self.marks + other.marks
    pass


nitin = Student("Nitin goswami", 83)
shayna = Student("Shayna Chhari", 87)

# here we got operator overloading by defining dunder method
print(nitin + shayna)















#**********

class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

        # print our string object

    def __repr__(self):
        return 'Object: {}'.format(self.string)

    def __add__(self, other):
        return self.string + other


# Driver Code
if __name__ == '__main__':
    # object creation
    string1 = String('Hello')

    # concatenate String object and a string
    print(string1 + ' Geeks')

