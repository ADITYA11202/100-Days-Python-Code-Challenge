# Question 1
n = int(input("Enter a number: "))
if(n %2== 0):
    print(f"The number {n} is even")
else:
    print(f"The number {n} is odd")

print("============================================")

# Question 2
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

if(a>b and a>c):
    print(f"{a} is the largest number")
elif(b>a and b>c):
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")

print("============================================")

# Question 3
p = int(input("Enter the value of principle: ")) 
r = int(input("Enter the value of rate: ")) 
t = int(input("Enter the value of time: ")) 
SI = (p * r * t)/100
print(f"The value of simple interest is {SI}")

print("============================================")