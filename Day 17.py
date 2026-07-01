# Concatenate the two string without using "+" operator
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = " ".join([str1,str2])
print(result)

print("=======================================")

# Print alternate chara of string
str3 = input("Enter the string: ")

new_string = ""
for i  in range(len(str3)):
    if (i == 0 or i  %2 == 0):
        new_string += str3[i]

print("Result = ",new_string)
        
print("=======================================")

# Checking a string contaning a substring
str4 = input("Enter the string: ")
subStr = input("Enter the substring: ")

if subStr in str4:
    print("Substring is present in string")
else:
    print("Substring is not present in string")
    