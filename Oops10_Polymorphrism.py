# The word polymorphism means having many forms.
# In programming, polymorphism means same function name but being uses for different types.
# Eg. of polymorphism
print(len("Shayna"))
print(len([10, 20, 30]))
# here function len used for string as well as for list


# Polymorphism in object oriented programming
class India:
    @staticmethod
    def capital():
        print("The capital is New Delhi")

    @staticmethod
    def language():
        print("Hindi is primary language in India")
    pass


class USA:
    @staticmethod
    def capital():
        print("The capital is Washington D.C")

    @staticmethod
    def language():
        print("English is primary language in India")
    pass


india = India()
usa = USA()

for country in [india, usa]:
    print(type(country))
    country.capital()
    country.language()

# Same method name but different outputs for different object it means here polymorphism is achieved here.
