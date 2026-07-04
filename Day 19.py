# Finding maximun and minimum number in list without using max() and min()
l1 = [29,20,24,98,2]
max = l1[0]
min = l1[0]
for i in l1:
    if i > max:
        max = i
    elif i < min:
        min = i

print("Maximum number is:",max)
print("Minimum number is:",min)

print("=============================================")

# Print only even number form list
l2 = [83,32,30,29,94,29,20]

for i in l2:
    if i %2 == 0:
        print("Even number = ",i)
    
print("=============================================")

# Reverse the list without using reverse() function
l3 = [39,32,30,89,85,58]

print("REverse list = ",l3[::-1])