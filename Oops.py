# spy number

# n = int(input("Enter any no "))
# s = 0
# p = 1

# while n > 0:
#     d = n%10
#     s = s+d
#     p = p*d
#     n = n//d

# print("Sum = ",s ,"Prod =",p)

# if s == p:
#     print("Number is a spy Number")
# else:
#     print("Number is not a spy Number")

print("==========Reverse Number============")
n = int(input("Enter any no: "))
r = 0

while n > 0:
    d = n % 10
    r = r*10+d
    n = n//10
print("Reverse = ", r)

print()

print("=======Palindrome=========")
n = int(input('Enter any no: '))
a = n
r = 0

while n > 0:
    d = n % 10
    r = r*10+d
    n = n//10
print("Reverse = ", r)
if a == r:
    print("Number is a Palindrome")

else:
    print("Number is not a Palindrome")

print()

print("========Armstong Number========")
n = int(input("Enter any no (3 digits) :"))
if n >= 100 and n <= 999:
    s = 0
    a = n
    while n > 0:
        d = n % 10
        s = s+d**3
        n = n//10
        print("sum = ", s)

        if a == s:
            print("Number is an ArmStrong")
        else:
            print("Number is not an ArmStrong")
else:
    print("Number is Invaild ,Enter 3 digits")

print()

print("========Strong Number============")
n = int(input("Enter any no (3 digit):"))

s = 0
a = n
while n > 0:
    d = n % 10
    f = 1
    i = 1
    while i <= d:
        f = f*i
        i += 1
    s = s+f
    n = n//10

    print("sum = ", s)

    if a == s:
        print("Number is a strong nos")
    else:
        print("Number is not a strong nos")
