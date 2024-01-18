sandwich_orders = ['Chicken Sandwich','pastrami','Egg Sandwich','pastrami','Seafood Sandwich','Grilled Cheese','pastrami']

# Empty list to store finished sandwiches.
done_sandwiches = []

print('We are sorry, the deli has run out of pastrami.','\n')

# Remove all 'pastrami' from the sandwich_orders list.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process the remaining sandwich orders.
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I am now making your {sandwich}.') # Print a message indicating that the sandwich is being made.
    done_sandwiches.append(sandwich)

print('\n')

for sandwich in done_sandwiches:
    print(f'I finished making your {sandwich}.')