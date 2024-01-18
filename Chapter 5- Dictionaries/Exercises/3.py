# Added five more Python terms to the glossary
Glossary = {
    'list': 'Ordered collection of items, changable.',
    'float': 'Data type for real numbers with a decimal point.',
    'string': 'Data type for a sequence of characters',
    'elif': 'Keyword for "else if" in conditional statements.',
    'print': 'Built-in function to display output.',
    'tuple' : 'Ordered, immutable collection of items.',
    'boolean' : 'Data type representing True or False values.',
    'dictionary' : 'Unordered collection of key-value pairs.',
    'function' : 'Reusable block of code, organized to perform a specific task.',
    'loop' : 'Repeated execution of a set of statements.'}



# Using a loop to print the meanings for each term in the Glossary dictionary
for term, meaning in Glossary.items():
    print(f'{term}: {meaning}\n')
