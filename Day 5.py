# Question 1

n = int(input("Enter a number: "))
if(n>0):
    print(f"The given number {n} is positive.")
elif(n==0):
    print(f"The given number {n} is zero.")
else:
    print(f"The given number {n} is negative.")

print("============================================")

# Question 2
year = int(input("Enter the year: "))
if(year %400 == 0) or (year %4 == 0 and year %100 != 0):
    print("It is leap year")
else:
    print("It is not leap year")

print("============================================")

# Question 3
import random

price = int(input("Enter the price of an item: "))
discount = random.choice([5,10,20])
print(f"The discount value you have taken: {discount}")

discount_percent = (price * discount)/100
final_price = price - discount_percent
 
print(f"The final price of an iteam is {final_price}") 

print("============================================")