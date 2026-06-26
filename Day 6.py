# Question 1
n = int(input("Enter the number: "))

if(n %3 == n% 5 == 0):
    print("It is multiple of 3 and 5")
elif(n %3 == 0 ):
    print("It is multiple of 3")
elif(n %5 == 0):
    print("It is multiple of 5")
else:
    print("It is not multiple of 3 and 5")

print("=================================")
# Question 2
for i in range(1,21):
    print(i) 

print("=================================")

# Question 3
a = 20
while a >= 1:
    print(a)
    a -= 1

print("=================================")
