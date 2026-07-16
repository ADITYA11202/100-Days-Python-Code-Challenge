# Build a number guessing game using the random module.
import random

computer = random.randint(1,100)
guesses = 0
user = -1
while (user != computer):
    guesses +=1
    user = int(input("Guess the number: "))

    if computer > user:
        print("highter number please")
    elif computer < user:
        print("lower number please")

print(f"You have guessed number correctly in {guesses} attempt")
print("Coumpter number = ",computer)

print("=========================================================")

# Take a list of number ad print how many are prime.
number = list(map(int,input("Enter the number: ").split()))

count = 0
for num in number:
    if num > 1 :
        is_prime = True

        for i in range(2,num):
            if num %i == 0:
                is_prime = False
                break
        
        if is_prime:
                count += 1

print("Number of prime number = ",count)

print("=========================================================")

# Take a string and check if all brackets in it are balanced (only one type, e.g. parentheses).


a = input("Enter the sentence including parentheses: ")

count = 0
balanced = True

for ch in a:
    if ch == "(":
        count += 1
    elif ch == ")":
        count -= 1

        if count < 0:
            balanced = False
            break

if balanced and count == 0:
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")

print("=========================================================")