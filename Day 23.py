# Rotate the element in list by one position 
l1 = list(map(int, input("Enter the list element: ").split()))
first = l1[0]
for i in range(len(l1)-1):
    l1[i] = l1[i+1]

l1[len(l1)-1] = first
print("Rotated list = ",l1)

print("=========================================")

# Find the index of first occurance of given element in list
l2 = list(map(int, input("Enter the list element: ").split()))
n = int(input("Enter the element to find: "))

for i  in range(len(l2)):
    if l2[i] == n:
        print("Occurance element is = ",l2[i])
        break
    else:
        print("Element not found")

print("=========================================")

# Print letter which lenght is greater than 3
l3 = list(map(str, input("Enter the list element: ").split()))
l4 = []
for word in l3:
    if len(word) > 3:
        l4.append(word)
    else:
        print("No word is greater than 3")

print("Letter which lenght is greater than 3 = ",l4)