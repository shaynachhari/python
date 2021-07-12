# exception handling or error handling
# a = input("Num1: ")
# b = input("Num2: ")

# try and finally always execute
# if error is occurs then except will execute otherwise else will execute
tup = 3, 6, 9
try:
    # print("before add")
    # print("The sum is:", int(a) + int(b))
    # print("after add")
    tup.insert(0, 3)
    # tup[21]

except IndexError as f:
    print("Index error found")

except AttributeError:
    print("Attribute Error found")

else:
    print("No error occurs")

finally:
    print("addition ends")

#************************************************************
# a = input("Num1: ")
# b = input("Num2: ")
# 
# try:
#      print("before add")
#      print("The sum is:", int(a) + int(b))
#      print("after add")
# 
# except:
#     print("i am except")
# 
# else:
#     print("i'am else")
# 
# finally:
#     print("i am finally")
num1 = input("please enter your 1st no.")
num2 = input("please enter your 2nd no. ")

try:
    print(f"the sum of the two number s : {int(num1)+int(num2)}")

except Exception:
    print(num1)
else:
    print("your successfully add two no.s ")

finally:
    print("Hello World !")
