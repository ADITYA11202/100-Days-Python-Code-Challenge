# Take a list of tuple and sort them based on the second element.
data = [("Rohan", 93), ("Aditya", 88), ("Rahul", 89), ("Athrva", 94)]

data.sort(key = lambda x:x[1])
print(data)

print("====================================================")

# Build a basic calculator that perform +,-,*,/ based on user choice.

print("1. Add")
print("2. Substract")
print("3. Multiple")
print("4. Divide")

choice = int(input("Enter your choice(1 - 4): "))

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

match choice:
    case 1:
        print("Addition = ",a+b)
    
    case 2:
        print("Substraction = ",a-b)

    case 3:
        print("Multiply = ",a*b)

    case 4:
        print("Divide = ",a/b)

print("====================================================")

# Take a number and print its multiplaction table from 1 to 10 using a function.
n = int(input("Enter the number: "))

def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}",)

table(n)

print("====================================================")