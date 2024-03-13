'''You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
Print a message to each of the two people still on your list, letting them know they're still invited.
Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.'''

party_invites = ['Emily', 'Bailey', 'Logan']

print(f"\nYou're invited, {party_invites[0].title()}!")
print(f"You're invited, {party_invites[1].title()}!")
print(f"You're invited, {party_invites[2].title()}!")
print(f"\nSorry, {party_invites[1].title()} can't make it to dinner.")
party_invites.insert(1, 'Liam')
print(f"\nYou're invited, {party_invites[1].title()}!")
print("\nWe found a bigger table!")

party_invites.insert(0, 'Ethan')
party_invites.insert(2, 'Adrian')
party_invites.append('Tyson')
print(f"\nYou're invited, {party_invites[0].title()}!")
print(f"You're invited, {party_invites[2].title()}!")
print(f"You're invited, {party_invites[6]}")

print("\nUnfortunately, the new table will not be ready in time. I can only invite 2 people.")
name = party_invites.pop()
print(f"\nSorry, {name.title()}, you are no longer invited.") 
name = party_invites.pop()
print(f"Sorry, {name.title()}, you are no longer invited.")
name = party_invites.pop()
print(f"Sorry, {name.title()}, you are no longer invited.")
name = party_invites.pop()
print(f"Sorry, {name.title()}, you are no longer invited.")
name = party_invites.pop()
print(f"Sorry, {name.title()}, you are no longer invited.")

print(f"Hey, {party_invites[0].title()}, you are still invited!")
print(f"Hey, {party_invites[1].title()}, you are still invited!")

del(party_invites[0])
del(party_invites[0])
print(party_invites)