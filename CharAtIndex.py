# Write a Python program that prints the character at index i in the string s.

# If the index is out of range, the program should print "i is out of range"

# If the string is empty, the program should print "Empty String"

str = input("Enter a string: ")

# str = "Print the character at index i in the string"

i = int(input("Enter an index value: "))

if str :
    if i >= 0 and i < len(str): 
        print('"', str[i], '"')
    else:
        print("i is out of range")
else: 
    print("Empty string")