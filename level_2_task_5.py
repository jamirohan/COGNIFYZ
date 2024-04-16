#LEVEL 2 TASK 5

# File Manipulation

filename = input("Enter file name: ")
f = open(filename, "r")
data = f.read()
count = {}
for char in data:
    if char != " ":
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
for key, value in count.items():
    print(f"{key}: {value}")
