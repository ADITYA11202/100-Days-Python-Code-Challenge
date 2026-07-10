# Questiion 1
n = int(input("Enter the number: "))
a = str(n)
d = a[::-1]
print("Reverse Number:",d)

print("==========================================")

# Question 2
num = int(input("Enter the number: "))
c = str(num)
rev = c[::-1]

if(c==rev):
    print("It is Palindrome")
else:
    print("It is not Palindrome")

print("==========================================")

# Question 3
A = int(input("Enter the number: "))
def sum(A):
    if A == 0:
        return 0
    return A + sum(A-1)

print("The sum of number is:",sum(A))
