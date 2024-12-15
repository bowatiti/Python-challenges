# Write a Python program that prints the first and last three characters of the string s as a single string.

# If the string has less than six characters, print an empty string (blank output).

str = input("Enter a string: ")

# slicing

if len(str) >= 6:
    print(str[:3] + str[-3:])
else:
    print("")