# Write the function to check the number is prime.len
def number(n):
    if n <=1 :
        print("THe number is not prime")
        return  
    
    for i in range(2,n):
        if n %i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")

number(4) 
number(13)

print("============================================")

# Create the function to calculate the factorial of number
n = int(input("Enter the number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial = ",factorial(n))

print("============================================")

# Create the function to check the string is palindrome
a = input("Enter the sentence: ")

def str(a):
    if a == a[::-1]:
        print("The string is Palindrome")
    else:
        print("The string is not palindome")

str(a)

print("============================================")