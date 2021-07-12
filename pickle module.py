import pickle

# dump method is used to pickle a object in a pickle file
# load method is used to unpickle a object from pickle file
# when we use pickle we have to open a file in binary type

lst = ["Shayna", "Nitin", "Love", "onesoul", "World"]
file = "achar.pkl"

# pickling
file_obj = open(file, "wb")
pickle.dump(lst, file_obj)
file_obj.close()

# unpickling
file_obj = open(file, "rb")
my_lst = pickle.load(file_obj)
print(my_lst)
file_obj.close()



#=====
lst = ["shayna","nitin","shivani","kashish","pallavi"]
file = "achr.pkl"

#packing
file_obj = open(file, "wb")
pickle.dump(lst,file_obj)
#print(file_obj)
file_obj.close()

#unpacking
file_obj = open(file,"rb")
my_lst = pickle.load(file_obj)
print(my_lst)
file_obj.close()
