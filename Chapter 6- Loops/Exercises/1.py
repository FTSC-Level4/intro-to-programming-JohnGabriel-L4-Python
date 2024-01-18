# I initialized an empty list 'toppings' to store the pizza toppings.
toppings = []

# I used a 'while' loop with 'True' condition to keep receiving toppings until the user decides to quit.
while True:
    # I used the 'input' function to get a pizza topping from the user.
    topping = input("Enter a pizza topping or 'quit' to finish: ")
     # I checked if the user entered 'quit'. If so, I broke out of the loop.
    if topping == "quit":
        break
    # I added the entered topping to the 'toppings' list and printed a confirmation message.
    toppings.append(topping)
    print("Added " + topping + " to your pizza.")

print("\nYour pizza will have the following toppings:")
# I used a 'for' loop to iterate through the 'toppings' list and print each topping.
for topping in toppings:
    print(topping)
