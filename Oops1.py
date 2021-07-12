class Students:
    name = "name"
    roll = 0
    cgpa = 0.0


nitin = Students()
shayna = Students()
nitin.name = "Nitin"
nitin.roll = "0904cs191051"
nitin.cgpa = "9.1"
nitin.income = 20000000
print(nitin.income)
# Students.cgpa = 5.3

shayna.name = "Shayna"
shayna.roll = "0904cs191071"

# print(nitin.roll)
# print(shayna.name)
# print(shayna.cgpa)
#
print(Students.__dict__)
print(nitin.__dict__)
