# Write a Python program that prints the string s without the characters located at even indices.

# If the string is empty or only has one character, print it intact.

str = input("Enter a string: ")

# slicing

if len(str) < 2:
    print(str)
else:
    print(str[1::2])

