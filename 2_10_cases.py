'''Use a variable to represent your favorite number. 
Then, using that variable, create a message that reveals your favorite number. Print that message.'''

favorite_number = 33
message = "My favorite number is " + str((favorite_number))

print(message)

# OR

favorite_number = 33
message = f"My favorite number is {favorite_number}"

print(message)

# F-strings are superior in readability as well as performance