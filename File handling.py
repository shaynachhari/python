"""
                File handling
mode - read, write, append
+a---> ra
+w---> rw
+r --> rw / ra
x--> file creation
type - binary(b) and text(t)
by default --> "rt"

--methods--
read mode -- read, readline, readlines
append mode -- write
write mode -- write
seek --> place the pointer
tell --> return place value of pointer

--IO functions, method and statement--
open --> file open/ or making file object
close --> file close/ closing file object
with...as --> statement used in place of open and close.

--using loop--
if we using loop in read mode on file object then we can easily get content of file without use of read_method
"""
file = "hello.txt"

file_obj = open(file, "rt")
var = file_obj.read()
print(var)
file_obj.close()

with open(file) as file_obj:
     print(file_obj.readline())
     # print(file_obj.read())
     print(file_obj.readline())
     print(file_obj.readline())

with open(file) as file_obj:
     print(file_obj.readlines())

s = 0
with open(file) as file_obj:
     for i in file_obj:
         if s == 7:
            break
         print(i)
         s += 1

with open(file, "rb") as file_obj:
     print(file_obj.read())

file = "info.txt"

with open(file, "wt") as file_obj:
     file_obj.write("Shayna")

with open(file, "at") as file_obj:
     file_obj.write("Nitin")
     file_obj.write("are one")

# used for creating a empty file
# file_obj = open("NS.txt", "x")
# file_obj.close()

with open(file, "w+") as file_obj:
     file_obj.write(" Hello baby")
     file_obj.seek(0)
     print(file_obj.read())

# with open(file, "+a") as file_obj:
#     file_obj.seek(0)
#     print(file_obj.read())
#     print(file_obj.tell())
#     file_obj.write(" Hello Sweetheart")
#     file_obj.seek(0)
#     print(file_obj.read())

# if we use +r mode then it shows anonymous behaviour.(anonymous=Anjana)
# so we avoid to use +r.
# instead of +r we can use +a or +w
# with open(file, "+r") as file_obj:
#     # print(file_obj.read())
#     file_obj.write("You are cute.")