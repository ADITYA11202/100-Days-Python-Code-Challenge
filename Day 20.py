# Count how many time given element appear in list
n = int(input("Enter the number: "))
l1 = [92,49,92,34,48,29,92]
count = 0

for i in l1:
    if n == i:
        count += 1
print("The number is: ",count)

print("=======================================")

# Find the second largest element in list
l2 = [29,282,38,22,480,290]
l2.sort()
print("Second last higgest value = ",l2[-2])

print("=======================================")

# Remove duplicate element from list
l3 = [82,93,84,29,29,58,93]
l4 = []
new_list = list(set(l3))
print("New list = ",new_list)

            # OR

for i in l3:
    if i not in l4:
        l4.append(i)

print("New list = ",l4)