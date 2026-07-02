# Counting letter in uppercase and lowercase
str1 = input("Enter the string: ")
count_upper = 0
count_lower = 0
for ch in str1:
    if ch.isupper():
        count_upper += 1
    else:
        count_lower += 1

print("Number of letter in uppercase = ",count_upper)
print("Number of letter in lowercase = ",count_lower)

print("=======================================================")

# Printing longest word in string
str2 = input("Enter the sentence: ")
words = str2.split()
largest = words[0]


for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word in sentence: ",largest)

print("=======================================================")

# Printing sum and average of list
l1 = [30,20,50,30,20]
# print(sum(l1))           My optional line(after writing code I had understand there is build in function to calculate the sum of list)

for i in l1:
    sum += i
    print("Sum = ",sum)
    

avg = sum/5
print("Avreage = ",avg)