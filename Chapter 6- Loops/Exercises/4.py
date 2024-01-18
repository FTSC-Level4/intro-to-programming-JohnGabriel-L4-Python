# I created a list 'sandwich_orders' and filled it with names of various sandwiches to be made.
sandwich_orders = ['Chicken Sandwich','Egg Sandwich','Seafood Sandwich','Grilled Cheese']
# I created an empty list 'finished_sandwiches' to store the completed sandwiches.
finished_sandwiches = []

# I used a 'for' loop to iterate through each type of sandwich in 'sandwich_orders'.
# For each sandwich, I printed a message indicating that it has been made.
# I then appended the sandwich to the 'finished_sandwiches' list.
for sandwich in sandwich_orders:
  print(f"I made your {sandwich}.")
  finished_sandwiches.append(sandwich)

  # I used '\n' to create a new line for better readability.
print("\nAll sandwiches have been made:")

# I used another 'for' loop to iterate through the 'finished_sandwiches' list.
# For each finished sandwich, I printed a message listing each sandwich that was made.
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")

