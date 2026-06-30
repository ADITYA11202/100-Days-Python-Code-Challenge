# Capitalize the word
str = input("Enter the sentance: ")

cap = str.title()
print(cap)

print("===============================")

# Checking if the word is anagram

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")

print("===============================")

# Remove all vowel from list
str3 = input("Enter the string: ")
result = ""
for ch in str3:
    if ch not in "aeiou":
        result += ch

print("After removing vowels = ",result)
