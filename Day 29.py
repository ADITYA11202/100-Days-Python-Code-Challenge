# Create a dictionary and check if a given key exists in it.
data = {
    "Rohan": 93,
    "Athrva": 94,
    "Aditya": 88,
    "Rahul": 89,
    "Satswarup": 99
}

name = input("Enter the name: ")

if name in data:
    print(True)
else:
    print(False)

    # OR

data = {
    "Rohan": 93,
    "Athrva": 94,
    "Aditya": 88,
    "Rahul": 89,
    "Satswarup": 99
}

name = input("Enter the name: ")
print(name in data)

print("========================================================")

# Merge two dictionaries into one.
a = {
    "Rohan": 93,
    "Athrva": 94,
    "Aditya": 88,
    "Rahul": 89,
    "Satswarup": 99
}

b = {
    "Shubham": 39,
    "Shivam": 38,
    "Ved": 83,
    "Amit": 82
}

print(a|b)

print("========================================================")

# Count the frequency of each character in a string using a dictionary.
string = input("Enter a string: ")

frequency = {}

for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)

print("========================================================")