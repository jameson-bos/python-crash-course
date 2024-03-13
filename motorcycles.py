motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Adding items to a list:
motorcycles.append('ducati')
print(motorcycles)

# Starting with an empty list, and building it dynamically:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Adding items to a specific position of the list:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.insert(2, 'ducati')
print(motorcycles)

# Removing items from a list, while knowing the specific position (deleting 'yamaha'):
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.insert(2, 'ducati')
del motorcycles[1]
print(motorcycles)

# Using the pop() method:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Demo of pop method:
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop()
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

# Giving a reason for removing from list:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")