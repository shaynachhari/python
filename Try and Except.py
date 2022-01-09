num1 = input("Please enter 1st number: ")
num2 = input("Please enter 2nd number: ")

try:
    print(f"The sum of these numbers is: {int(num1)+int(num2)}")
except Exception as a:
    print(a)
else:
    print("congratulations You have successfully add two numbers")
finally:
    print('Hello')
