# 1. creat a dictionary and take input from the user return the meaning of the world_from the dictionary

'''dict = {"shayna": "chhari" , "class":"14th" , "age":"18th", "status":"student"}
print(dict)

d2 = input()
print(d2[dict])'''










# Exercise 2 - Faulty Calculator
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print('                                         calculator')
print('                                         ----------')

a = input("Please enter the operation ")

b = float(input("please enter 1st number "))
c = float(input("please enter 2nd number "))

if a == '+' :
   if  b == 56 and c == 9:
    print("77")
   else:
       print(b+c)

elif a == '*':
    if b == 45 and c == 3:
        print("555")
    else:
        print(b*c)

elif a == '/':
    if b == 56 and c == 6:
        print("4")
    else:
        print(b/c)

elif a == '-':
    print(b-c)

else:
    print("Error! , please enter your vaild operator")