a = input("Enter your Operator : ")
b = int(input("Enter your 1st Number : "))
c = int(input("Enter your 2nd Number : "))

if a =='+':
    print(f"Sum of Two Number b+c => ",b+c)

elif a == '-':
    print(f"Sum of Two Number b-c => ",b-c)

elif a == '*':
    print(f"Sum of Two Number b*c => ",b*c)

elif a == '/':
    print(f"Sum of Two Number b/c => ",b/c)

elif a == '%':
    print(f"Sum of Two Number b%c => ",b%c)

else:
    print("Invalid Your Operator")
input()