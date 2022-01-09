dict = {"key1": "Nitin", "key2": "love", "key3": "Shayna"}
print(dict) #this will print a whole dict.

print(dict["key1"], dict["key2"], dict["key3"])   #This will print key value as indexing of dict
print(dict.values())   #this will prints values in tupple
print(dict.keys())  #this will prints keys in tupple
print(dict.__sizeof__())
dict1={"a": "N", "b": "L", "c": "S"}
print(dict1["a"],dict1["b"],dict1["c"])
dict2={(8,9,7):(1,2,3),"key2":(4,5,6),"key3":(9,8,7)}
print(dict2["key3"][0])
print(dict2.keys())
print(dict2["key3"][0])
dict3 = {(8, 9, 7): (1, 2, 3), "key2": (4, 5, (11, 12, 13)), "key3": (9, 8, 7)}
print(dict3["key2"][2][1])