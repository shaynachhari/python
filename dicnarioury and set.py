'''d1 = {}
print(type(d1))
d2 = {
    "name":"shayna",
    "age":"18" ,
    "colour":"black",
    "hobby":"dance",
    "goal":"bestjob",
    "shanu" : {"B":"maggie" , "L":"pasta", "R":"Rice"}
}
print(d2)
print(d2["shanu"])

d2["nitin" ] = "best friend"
d2["420"] = "uday"
print(d2["nitin"])
print(d2["420"])
print('\n')

d3 = d2.copy()
print(d3)

del d3["hobby"]
print(d3)
print('\n')
print(d2.items())
print(d2.keys())
print(d2.values())'''

# dic funtion all
'''d3 = {"name":"shani","food":"water balls","drink":"coffee","school":"gw"}
print(d3.items())
print(d3.keys())
print(d3.values())
print("\n")
d3.update({"school" : "ambah"})
print(d3)
d2=d3.pop("food")
print(d2)
d3.copy()
print(d3)
print('\n')
d3.clear()
print(d3)'''
# fromkeys() , popitem() , get()






## set all function
s = set()
print(type(s))

s_from_list = {3,5,6,7,8,9,11,22,35}
print(type(s_from_list))
s.add(1)
s.add(2)
print(s)
s2 = s.union({1,2,3,4,6,8})
print(s2)
s1 = s.intersection({1,2,3})
print(s1)

s1 = {4,6}
print(s.isdisjoint(s1))
s1.remove(4)
print(s1)


'''s1 = {2,3,4,5,6,7,8,9,12,36}
s2 = {4,6,12,34,12,14,55,35}

print(s1 & s2)  # intersection
print(s1 | s2)  # union
print(s1 ^ s2)  # jo dono ko milakar ek baar aaya hai
print(s1 - s2)
print(s2-s1)
for i in s_from_list:
    print(i)'''
a={1,5,2}
a.add(4)
a.add(3)
print(a)
s=set()
#for string
s.add("Nitin")
print(s)
s.add("Shayna")
print(s)
s.add("Avrity")
print(s)
ns=set(["Nitin","Love","Shayna"])
print(type(ns))
print(ns)
ns.add("one soul")
print(ns)
n=set()
n.add(1)
n.add(2)
n.add(3)
print(n)
l=n.union({2,3,4})
print(l)
o=n.intersection({8,9,1,2})
print(o)
print(ns)
ns.remove("one soul")
print(ns)
for c in ns:
    print(c, end=" ")
print(type(a))
a={"Nitin","Love","Shayna"}
l={1,5,2, "nitin", "shayna"}
print(l)






