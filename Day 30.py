# Take the list of words and create a dictonary with word lenght as value.
l1 = ["aditya","satswarup","rohan","rahul","athrva","shubham"]

a = {}
for word in l1:
    a[word] = len(word)

print("New dictonary = ",a)

print("=================================================")

# Find the key with maximum value in dictonary.
data = {
    "rahul":83,
    "rohan":93,
    "satswarup":94,
    "ved":100
    }

max_key = ""
max_value = 0

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("The with maximum value = ",max_key)
print("Maximum value = ",max_value)

print("=================================================")

# Create a tuple and unpack its values into seperate variable.
student = ("Aditya",20,"Pune")

name, age, city = student

print("Student name = ",name)
print("Student age = ",age)
print("City name = ",city)

print("=================================================")