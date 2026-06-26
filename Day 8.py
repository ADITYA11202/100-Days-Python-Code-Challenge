# Question 1

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} * {i} = { n * i }")

print("================================")

# Question 2
a = int(input("Enter the number: "))
def factorial(a):
    if a == 0 or a == 1:
        return 1
    return a * factorial(a-1)

print(f"The factorial of given number is : {factorial(a)}")

print("================================")

# Question 3
str = input("Enter anything: ")

print(len(str))