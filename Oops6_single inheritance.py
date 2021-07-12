# Inheritance
# Inheritance is a property in which child class inherit all properties from parent class
# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
class Country:
    population = "NA"
    area = "NA"

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        pass

    def detail(self):
        print(f"{self.name} has {self.population} population and have area {self.area}")
        pass
    pass


india = Country("India", "1280000000", "3287623 sq. kilometer")
india.detail()


class State(Country):
    capital = "NA"

    def __init__(self, name, population, area, capital):
        # Country.__init__(self, name, population, area)
        super().__init__(name, population, area)
        # super function is used to inherit the init_method(constructor) from parent class
        self.capital = capital

    def state_detail(self):
        print(f"{self.name} has {self.area} and have population {self.population}. Its capital is {self.capital}")
    pass


mp = State("Madhya pradesh", "7.33 crore", "308245 km sq.", "Bhopal")
mp.state_detail()

mp.detail()
