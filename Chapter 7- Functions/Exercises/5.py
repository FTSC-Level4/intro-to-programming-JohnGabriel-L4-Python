 #I defined a function 'describe_city' with default values for city and country.
def describe_city(city= 'New York', country = 'America'):
    # I used an f-string to print a message describing the city and its country.
    print(f'{city} is in {country}')

# I called the function with default values for city and country.
describe_city()
# I called the function again, this time specifying a different city while keeping the default country.
describe_city('Los Angeles')
# I called the function with specific values for both city and country.
describe_city('Tokyo', 'Japan')


