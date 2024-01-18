def make_shirt(size = 'Large', text = 'I Love Python'):
        # I used an f-string to print a message about the shirt size and the printed message.
    print(f'The size of this shirt is {size} and the message printed on it is "{text}".')

# I called the function with default values for size and text.
make_shirt()
# I called the function again, this time specifying a different size while keeping the default text.
make_shirt(size = 'Medium')

# I called the function with specific values for both size and text.
make_shirt(size = 'Small', text = 'I Love Earth')


