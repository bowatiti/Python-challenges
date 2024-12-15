# Write a Python Program that prints the reversed version of a string.

# The program must preserve uppercase and lowercase letters.

# If the string is empty, print it intact.

# slicing

str = input("Enter a string: ")

# rev = str[::-1]

# print('"',rev,'"')

# using loop

revLoop = ""

for i in str:
    revLoop = i + revLoop

print('"',revLoop,'"')
