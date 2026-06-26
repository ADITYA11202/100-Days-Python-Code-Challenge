# Fibonacci Series
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("================================")

# Check Number is Perfect square 
num = int(input("Enter the number: "))
for i in range(1,num+1):
    if (i * i == num):
        print(f"{i} is a perfect square of {num}")
        break
else:
    print("It is not perfect square")

print("================================")

# Number Divisible by 7
for i in range(1,101):
    if (i%7==0):
        print(i,end=" ")

