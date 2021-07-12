# In multilevel inheritance, there are one parent class one child class
# which is also a parent class for another child class

class Computer:
    ram = "4 gb"
    ssd = "1 tb"

    def __init__(self, ram, ssd):
        self.ram = ram
        self.ssd = ssd
        pass

    def hardware(self):
        print(f"The ram: {self.ram} and internal memory: {self.ssd}")
        pass
    pass


class Cpu(Computer):
    ram = "8 gb"
    ssd = "1 tb"
    fan = "500 Rpm"

    def __init__(self, ram, ssd, fan):
        super(Cpu, self).__init__(ram, ssd)
        self.fan = fan
        pass

    def cpu_detail(self):
        print(f"The ram: {self.ram}, internal memory: {self.ssd} and fan: {self.fan}")
    pass


class Processor(Cpu):
    name = "intel core i3"
    generation = "3rd generation"

    def __init__(self, name, generation):
        self.name = name
        self.generation = generation
        pass

    def processor_detail(self):
        print(f"Processor name is {self.name} and generation is {self.generation}")
    pass


i5 = Processor("intel core i5", "5th generation")
i5.ram = "9gb"
i5.processor_detail()
i5.hardware()
print(i5.ram)
