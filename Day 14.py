# Replacing spaces by underscore
l = input("Enter the string: ")
a = l.replace(" ","-")
print(a)

print("===========================")

# Starting with vowel
l1 = input("Enter the string: ")

if l1[0].lower() in "aeiou":
        print("It start with vowel")
else:
        print("It not start with vowel")
print(l1[0])

print("===========================")

# Counting specific chara in string
l2 = input("Enter the string: ")
ch = input("Enter the chara: ")

print("Number of occurance = ",l2.count(ch))

            #    OR
            
count = 0
for i in l2:
        if i == ch:
                count += 1
print("Number of occurance = ",count)