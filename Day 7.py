# Question 1
n = int(input("Enter the number: "))
def sum(n):
    if n == 1:
        return 1
    c = n + sum(n-1)
    return c

sum(n)
print(f"The sum of the number {n} is: {sum(n)}")

print("===========================================")

# Question 2

for i in range(1,51):   #for i in range(2,51,2):
     if (i %2 == 0):    #       print(i)
        print(i)

print("===========================================")

for i in range(1,51,2):
    print(i)

print("===========================================")    