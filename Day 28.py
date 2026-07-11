year = int(input("Enter the year: "))

def leap_year(year):
    if year %4 == 0:
        return True
    elif year %100 == 0:
        return True
    elif year %400 == 0:
        return True
    else:
        return False

print(leap_year(year))

print("==================================================")

# Create the dictionary of students and print the key-value pair
a = {
    "Rohan": 93,
    "Ruhul": 88,
    "Aditya": 100,
    "Satswarup": 100,
    "Shivam": 90
}

print(a)

print("==================================================")

# Create the dictionary print only the key, then only the values.
b = {
    "Ved": 93,
    "shubham": 98,
    "Athrva": 92,
    "Mansi": 83,
    "Shatakshi": 92
}

print("Keys = ",b.keys())
print("Values = ",b.values())

print("==================================================")
