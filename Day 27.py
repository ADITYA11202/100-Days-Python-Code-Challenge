# Create the function that return the nth Ficonacci number
n = int(input("Enter the number: "))

def fab(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)
    
print("Ficonacci number = ",fab(n))

print("================================================")

# Create the function to check the number is Armstrong
num = input("Enter the number: ")

def Armstrong(num):
    power = len(str(num))
    total = 0

    for digit in str(num):
        total += int(digit) ** power
    return total
    
total = Armstrong(num)

if total == int(num):
    print("The number is Armsteong")
else:
    print("The number is not armstrong")

print("================================================")

# Create the function to count vowel and consonant in string
str = input("Enter the string: ")

def Vowel_or_Consonant(str):
    count_vowel = 0
    count_consonant = 0

    for ch in str:
        if ch.isalpha():
            if ch in "aeiou":
                count_vowel += 1
            else:
                count_consonant += 1
    return count_consonant , count_vowel

count_consonant, count_vowel = Vowel_or_Consonant(str)

print("Vowels = ",count_vowel)
print("Consonants = ",count_consonant)

print("================================================")