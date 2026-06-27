# Sum of Square of N natural number
n = int(input("Enter the number: "))

sum = 0
for i in range(1,n+1):
    sum = sum + i*i

print("Sum of Square = ",sum)

print("=================================")

# String Length
a = input("Enter the string: ")

print("The length of string = ",len(a))

print("=================================")

# Reverse the string
b = input("Enter the string: ")
print("Reversing the string = ",b[::-1])