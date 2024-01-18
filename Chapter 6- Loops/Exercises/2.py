# This loop will continue until the user enters 'quit'.
while True:
    # Prompt the user to enter their age.
    age_input = input("Please enter your age (type 'quit' to exit): ")

    # Check if the user wants to quit.
    if age_input.lower() == 'quit':
        break
    age = int(age_input)

    # Determine the ticket price based on the age.
    if age < 3:
        ticket_price = 0  # Ticket is free for age less than 3.
    elif 3 <= age <= 12:
        ticket_price = 10  # Ticket costs $10 for ages between 3 and 12.
    else:
        ticket_price = 15  # Ticket costs $15 for ages over 12.

    # Display the cost of the movie ticket to the user.
    print(f"The cost of your movie ticket is ${ticket_price}.\n")
