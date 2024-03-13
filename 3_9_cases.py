'''Working with one of the programs from Excersises 3-4 thru 3-7, 
use len() to print a message indicating the mumber of people you're inviting to dinner'''


# Original code
party_invites = ['Emily', 'Bailey', 'Logan']

print(f"You're invited, {party_invites[0].title()}!")
print(f"You're invited, {party_invites[1].title()}!")
print(f"You're invited, {party_invites[2].title()}!")

# Using len()
number_of_invites = len(party_invites)
print(f"The total number of invites are {number_of_invites}.")