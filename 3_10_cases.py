''' Think of things you could store in a list. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
FUNCTIONS NEEDED TO BE USED: append(), insert(), pop(), remove(), sort(), sorted(), reverse(), len()'''

# Date Ideas - hike, picnic, movies

dates = []

# Append method
dates.append('hike')
dates.append('picnic')
dates.append('movies')
print("\nHere is the list of date ideas so far:")
print(dates)

# Insert function
print("\nLet's add another date idea in the second position of the list:")
dates.insert(1, 'drive')
print(dates)

# Pop function
print("\nI don't like the last date idea in the list, let's remove it: ")
dates.pop()
print(dates)

# Add movies back
print("\nI've been convinced to go to the movies:")
dates.append('movies')
print(dates)

# Remove method
print("\nHikes are tiring, let's remove it:")
dates.remove('hike')
print(dates)

# Len method
print("\nHow many date ideas do we have now?")
print(f"Currently, we have, {len(dates)}, dates.")

# Sorted method
print("\nLet's temporarily sort this list in alphabetical order:")
print(sorted(dates))

# Non sorted list again
print("\nAnd here's the non sorted list again:")
print(dates)

# Sort method
print("\nLet's permamently sort the list in alphabetical order:")
dates.sort()
print(dates)

# Reverse method
print("\nNow that the list is in alphabetical order, let's permamently sort the list in reverse alphabetical order:")
dates.reverse()
print(dates)