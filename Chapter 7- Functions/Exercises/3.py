# I defined a function
def make_shirt(size, text):
    # I used an f-string to print a message about the shirt size and the printed message
    print(f'The size of this shirt is {size} and the message printed on it is "{text}".')

# I called the function with specific values for size and text.
make_shirt('Medium', 'I love Earth')

# I called the function again, this time using keyword arguments to specify size and text.
make_shirt(text = 'I Hate Earth', size = 'small')


