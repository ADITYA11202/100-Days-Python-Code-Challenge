# Insert a number in sorted list while keeping it sorted.
l1 = [10,20,30,40,50,60]
n = int(input("Enter the number: "))

for i in range(len(l1)):
    if n < l1[i]:
        l1.insert(i, n)
        break
else:
    l1.append(n)

print("Updated list = ",l1)

print("============================================")

# Take a list and remove all the occurance in list
l2 = list(map(int,input("Enter the number: ").split()))
num = int(input("Enter the number: "))

for  number in l2:
    if number == num:
        l2.remove(num)

print("Updated list = ",l2)

print("============================================")

# Check a duplicate element in list
l3 = list(map(int, input("Enter the number: ").split()))
duplicate = False

for i in range(len(l3)):
    for j in range(i+1,len(l3)):
        if l1[i] == l1[i]:
            duplicate = True
            break
    if duplicate:
            break
if duplicate:
        print("The list contain duplicate element")
else:
        print("The list does not contain  duplicate element")

print("============================================")