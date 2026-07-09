# Create the function that make list and print sum of all element.
n = list(map(int,input("Enter the number: ").split()))

def total_sum(n):
    total = 0
    for i in range(len(n)):
        total = total + n[i]
    return total

print("sum of element = ",sum(n))

print("=================================================================")

# Create the function to convert Celsius to Fahrenheit and vice versa.
def Celsius_to_Fahrenheit(C):
    fahrenheit = (C * 1.8) + 32
    return fahrenheit

def Fahrenheit_to_Celsius(F):
    celsius = (F - 32) + 5/9
    return celsius


choice = int(input("Enter 1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius:" ))

if choice == 1:
    C = float(input("Enter the temperature in Celcius: "))
    print("Temprature in fahrenheit = ",Celsius_to_Fahrenheit(C))

elif choice == 2:
    F = float(input("Enter the tempraure in Fahrenheit: "))
    print("Temprature in celsius = ",Fahrenheit_to_Celsius(F))

else:
    print("Invalid Choice")

print("=================================================================")

# Create the function to calculate the area of different shapes.

def Circle(r):
    Area = 3.14 * r * r
    return Area

def Square(side):
    Area = side * side 
    return Area

def Rectangle(l,w):
    Area = l * w
    return Area

New_Choice = int(input("Enter 1 for Circle or 2 for Square or 3 for Rectangle: "))

if New_Choice == 1:
    r = float(input("Enter radius of circle: "))
    print("Area of circle = ",Circle(r))

elif New_Choice == 2:
    side = float(input("Enter the side of Square: "))
    print("Area of Square = ",Square(side))

elif New_Choice == 3:
    l = float(input("Enter the lenght of reactangle: "))
    w = float(input("Enter the width of reactangle: "))
    print("Area of Rectanglre = ",Rectangle(l,w))

else:
    print("Invalid Choice")