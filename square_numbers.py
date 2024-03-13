squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

#
squared_numbers = []
for number in range(1, 6):
    square_number = number ** 2
    squared_numbers.append(square_number)

print(squared_numbers)

#
powered_numbers = []
for number in range(1,100):
    threes = number ** 3
    powered_numbers.append(threes)

print(powered_numbers)

# Lines 25-35 print the same thing - Is there a problem with using the same variable in the for loop?
squared_numbers = []
for number in range(1,6):
    number = number ** 2
    squared_numbers.append(number)
print(squared_numbers)

squares = []
for value in range(1, 6):
    square = value ** 2
    squares.append(square)
print(squares)

# More concise
squared_numbers = []
for value in range(1,6):
    squared_numbers.append(value ** 2)
print(squared_numbers)