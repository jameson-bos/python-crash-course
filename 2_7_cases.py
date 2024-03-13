'''Use a variable to represent a person's name, and include some whitespace at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().'''

person_name = ' \tJameson Bos\n    '

print("Unmodified:")
print(person_name)

print("lstrip():")
print(person_name.lstrip())

print("rstrip():")
print(person_name.rstrip())

print("strip():")
print(person_name.strip())
