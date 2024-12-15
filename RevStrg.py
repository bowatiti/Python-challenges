# slicing

str = input("Enter a string: ")

# rev = str[::-1]

# print('"',rev,'"')

# using loop

revLoop = ""

for i in str:
    revLoop = i + revLoop

print('"',revLoop,'"')
