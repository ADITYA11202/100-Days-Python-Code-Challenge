# Printing digits present in string

text = input("Enter a string: ")

for ch in text:
    if ch.isdigit():
        print(ch, end="")
    print()

print("==========================")

# Finding most frequent chara in string
str = input("Enter the string: ")
max_count = str[0]

for ch in str:
    if str.count(ch) > str.count(max_count):
        max_count = ch
print("Most frequent chara : ",max_count)
print("Frequency : ",str.count(max_count))

print("==========================")

# ataking only alphabate
text = input("Enter a string: ")

for ch in text:
    if ch.isalpha():
        print(ch, end="")
    