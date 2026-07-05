# Sum of all even number in list
l1 = [8,2,4]
sum = 0

for number in l1:
    if number %2 == 0:
        sum = sum + number

print("The sum of even number in list = ",sum)

print("===============================================")

# Seperate the list into positive and negative number.
l2 = [83,84,-28,93,-3,29,-48,84,-47,37]
positive_list = []
negative_list = []

for number in l2:
    if number > 0:
        positive_list.append(number)
    else:
        negative_list.append(number)

print("Positive List = ",positive_list)
print("NEgative List = ",negative_list)

print("===============================================")

# Find common element in two list
l3 = [83,84,59,39,29,38,88]
l4 = [94,48,43,42,88,29,47]

for number in l3:
    if number in l4:
        print(number)