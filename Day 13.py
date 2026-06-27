# Converting the string into Uppercase and Lowercase
a = input("Enter the string: ")
print("Upper Case = ",a.upper())
print("Lower Case = ",a.lower())

print("=====================================")

# Counting gievn number of words in sentence
sen = input("Enter any sentence: ")
words = sen.split()
count = len(words)
print("Number of word = ",count)

print("=====================================")

# Printing first and last chara of string
str = input("Enter the string: ")
print("First Chara = ",str[0])
print("Last Chara = ",str[-1])