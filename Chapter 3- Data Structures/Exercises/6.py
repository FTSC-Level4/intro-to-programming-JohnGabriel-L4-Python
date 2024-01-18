# I created a list 'Guests' with names: Grandpa, Grandma, and Uncle.

Guests = ['Grandpa', 'Grandma', 'Uncle']

# I used a 'for' loop to iterate over each guest in the list.
# During each iteration, the variable 'g' holds the current guest's name.
for g in Guests:
    # I printed an invitation for each guest.
    print(f'I am inviting you to come join me for dinner, {g}.')

# I indicated that Uncle couldn't make it to dinner.
print(f"{Guests[2]} couldn't make it to dinner.")

# I updated the guest list by replacing 'Uncle' with 'Cousin'.
Guests[2] = 'Cousin'

# I used another 'for' loop to re-invite each guest with the updated list.
for g in Guests:
    print(f'I am inviting you to come join me for dinner, {g}.')

# I found out that the new dinner table won't arrive in time, so I can only invite two guests.
print("Unfortunately, the new dinner table won't arrive in time, and I can only invite two people for dinner.")

# I used pop() to remove guests from the list until only two names remain.
removed_guest = Guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

removed_guest = Guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# I printed a message to each of the two remaining people still on the list, letting them know they're still invited.
for remaining_guest in Guests:
    print(f"You're still invited to dinner, {remaining_guest}.")

# I used del to remove the last two names from the list, leaving an empty list.
del Guests[:]

# I printed the list to confirm that it is empty.
print(Guests)
