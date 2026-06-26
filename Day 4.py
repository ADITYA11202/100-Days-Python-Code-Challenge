# Question 1
age = int(input("Enter the age of person: "))
if(age>=18):
    print("The person is eligible for voting")
else:
    print("The person is not eligible for voting")

print("============================================")    

# Question 2
maths = int(input("Enter the marks: "))
english = int(input("Enter the marks: "))
bxt = int(input("Enter the marks: "))

average = (maths + english +bxt)/3

print(f"The average of threr subject marks is {average}")

print("============================================")

# Question 3
length = int(input("Enter the length of rectangle: "))
breath = int(input("Enter the breath of rectangle: "))

print(f"The area of rectangle is: {length * breath}")
print(f"The perimeter of rectangle is: {2*[length + breath]}")

print("============================================")