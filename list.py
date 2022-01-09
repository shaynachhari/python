s = [1, 2, 3, 4, 5, 6, 7]
print(type(s))
print(s)
print(s[1])
print(s[::-1])
print(s[1:3:])
n = ['Nitin', 'love', 'Shayna']
print(n[0], n[1], n[2])
print('_______________________________________________________')
print("___________list functions_____________")
ns = [4, 'Nitin', 'love', 'Shayna', 26, 24,]
ns.append(58)#this function is used for adding object at the end of the list
print(ns)
ns.insert(0,"one soul") #this is function is used for adding object at the any place of the list
print(ns)
ns[2]="Nik"
print(ns)
sn=['Nik', 'Shayna', 'Nitin', 'Kimmi']
sn.sort()#this function is used for sort the str and int in the list
print(sn)
nls = [8, 65, 895, 2, 0, 7, 3, 4, 6, 5]
nls.sort()
print(nls)
print(len(ns))#used for length of list
print("_______list remove functions________")
print(ns)
l = ns.pop(1)
print(ns)
print(l, ns)
ns.remove('one soul')
print(ns)
del ns[3]
print(ns)
ns[3] = 2
print(ns)
list = [8, 65, 895, 2, 0, 7, 3, 4, 6, 5]
z = len(list)
print(z)
print(list.__sizeof__())



####pop _function detials
# Python3 program for pop() method

list1 = [1, 2, 3, 4, 5, 6]

# Pops and removes the last element from the list
print(list1.pop())

# Print list after removing last element
print("New List after pop : ", list1, "\n")

list2 = [1, 2, 3, ('cat', 'bat'), 4]

# Pop last three element
print(list2.pop())
print(list2.pop())
print(list2.pop())

# Print list
print("New List after pop : ", list2, "\n")
list1 = [1, 2, 3, 4, 5, 6]

# Pops and removes the last
# element from the list
print(list1.pop(), list1)

# Pops and removes the 0th index
# element from the list
print(list1.pop(0), list1)