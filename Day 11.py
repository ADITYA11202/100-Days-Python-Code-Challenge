# GCD of given number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)

print("==================================")

# Simple * Pattern 
num = int(input("Enter the number: "))

for i in range(1,num+1):
    print("*"*i)

print("==================================")

# Simple number Pattern
n = int(input("Enter the number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j ,end=" ")
    print() 