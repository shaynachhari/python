# In multiple inheritance, there are two parent classes and one child class
class Country:
    name = "Country name"
    population = None
    area = None

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
# india.detail()


class Ocean:
    name = "Ocean name"
    ocean_name = "NA"

    def __init__(self, name, depth):
        self.ocean_name = name
        self.depth = depth
        pass

    def ocean_detail(self):
        print(f"{self.ocean_name} whose depth is ")
    pass


# parent class order is important when we create child class
# the fist parent class get higher priority than second parent class
class Place(Ocean, Country):
    name = "Place name"

    def __init__(self, name, area, population, pincode):
        Country.__init__(self, name, area, population)
        self.pincode = pincode
        pass
    pass


mp = Place("Madhya pradesh", "5487654", "565648485km sq", "476111")
print(mp.name)
