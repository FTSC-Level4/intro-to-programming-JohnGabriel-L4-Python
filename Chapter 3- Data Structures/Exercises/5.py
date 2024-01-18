# I created a list 'Guests' with names: Grandpa, Grandma, and Uncle.
Guests= ['Grandpa','Grandma','Uncle']

# I used a 'for' loop to iterate over each guest in the list.
for g in Guests:
     # I printed an invitation for each guest.
    print(f'I am inviting you to come join me for dinner',(g))

# I indicated that Uncle couldn't make it to dinner.
print({Guests[2]},"Couldn't make it to dinner")

# I updated the guest list by replacing 'Uncle' with 'Cousin'.
Guests[2]= 'Cousin'

# I used another 'for' loop to re-invite each guest with the updated list.
for g in Guests:
    print(f'I am inviting you to come join me for dinner',(g))
