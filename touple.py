tup = 1, 2, 3, 4
print(tup)
# tup[0]=9  ====> this will get an error are immutable which means we can not change value of tuple


tup1 = (1, 2, 3, 4)
print(tup1)  # prenticies are not so required in tupples but for stuctural pragraming we should use them
# tup.insert(0,5) ==> this will get an error because tuples  are immutable which means we can not change value of tuple
print(tup)
tup3 = (5, 8, "Nitin", 7, 4, 8)
del tup3  # this function is used to deleting a tuple
tup3 = (5, 5, 6, 6, 74, 8, 8)
print(tup3)

#***********************************************
#GETTING THE COUNT OF
tup1 = (3,4,5,6,'shayna','41',51,61,3,33,3,3,'shayna')
print(tup1)
tup2 = tup1.count('shayna')
print(tup2)

# Creating tuples
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2,21)
# getting the index of 3
res = Tuple.index(21)
print(res)
