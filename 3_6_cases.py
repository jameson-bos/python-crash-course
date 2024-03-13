'''You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

Start with your program from Exercise 3-4 or Exercise 3-5. 
Add a print() call to the end of your program, informing people that you found a bigger dinner table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list. Print a new set of invitation messages, one for each person in your list.'''

party_invites = ['Emily', 'Bailey', 'Logan']

print(f"\nYou're invited, {party_invites[0].title()}!")
print(f"You're invited, {party_invites[1].title()}!")
print(f"You're invited, {party_invites[2].title()}!")
print(f"\nSorry, {party_invites[1].title()} cannot make it to dinner.")
party_invites.insert(1, 'Liam')
print(f"\nYou're invited, {party_invites[1].title()}!")
print("\nWe found a bigger table!")

party_invites.insert(0, 'Ethan')
party_invites.insert(2, 'Adrian')
party_invites.append('Tyson')
print(f"\nYou're invited, {party_invites[0].title()}!")
print(f"You're invited, {party_invites[2].title()}!")
print(f"You're invited, {party_invites[6]}")