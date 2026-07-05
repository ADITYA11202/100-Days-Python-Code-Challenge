# Murge two list and sort the list
l1 = [93,393,292,94,493]
l2 = [83,29,439,349,92,39]

l1.extend(l2)
print("New list = ",l1)

l1.sort()
print("Sorte list = ",l1)

print("============================================")

# Print element of list placed at even indices only.
l3 = [93,39,29,22,20,88]

for i in range(len(l3)):
    if i %2 == 0:
        print(l3[i])

print("============================================")

# Check list is sorted or not.
l4 = [29,4,34,95,20,2,9]

if l4 == sorted(l4):
        print("The list is sorted")
else:
        print("The list is not sorted")

print("============================================")