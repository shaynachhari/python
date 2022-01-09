def factorial(num):
    if num == 1 or num == 0:
        return 1

    return num*factorial(num-1)


print("\t\t\tFactorial calculation")
n = int(input("Please enter the number for factorial: "))
print("The result is:", factorial(n))

# num*factorial(num-1)
# 5*factorial(5-1) => 5*factorial(4)
# 5*4*factorial(4-1) => 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1 = ans