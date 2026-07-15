# Print all prime number between 1 to 100.
for num in range(2,101):
    is_prime = True

    for i in range(2,num):
        if num%i== 0:
            is_prime = False
            break
    if is_prime:
        print(num,end=" ")
print()
        
print("===================================================")

# Take a sentance and count the number of vowel, consonent, digits, and spaces
sentence = input("Enter the sentance: ")

count_consonent = 0
count_digit = 0
vowel = "aeiou"
count_vowel = sum(sentence.count(v) for v in vowel)
count_spaces = sentence.count(" ")

for ch in sentence:
    if ch.isalpha() and ch not in vowel:
        count_consonent += 1

for ch in sentence:
    if ch.isdigit():
        count_digit += 1

print("Number of vowel = ",count_vowel)
print("Number of consonant = ",count_consonent)
print("Number of digit = ",count_digit)
print("Number of spaces = ",count_spaces)
 
        #    OR
count_spaces = 0
count_vowel = 0

for ch in sentence:
    if ch in "aeiou":
        count_vowel += 1
    elif ch.isalpha():
        count_consonent += 1 
    elif ch.isdigit():
        count_digit += 1
    elif ch == " ":
        count_spaces += 1

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Number of vowel = ",count_vowel)
print("Number of consonant = ",count_consonent)
print("Number of digit = ",count_digit)
print("Number of spaces = ",count_spaces)

print("===================================================")

# Create the simple grading system.
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 40:
    print("Grade: E")
else:
    print("Grade: F")

print("===================================================")