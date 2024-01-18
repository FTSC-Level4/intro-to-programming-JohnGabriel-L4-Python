# I printed a statement for each river and its associated country.
rivers = {'Mississippi River': 'United States',
          'Amazon River' : 'Brazil',
          'Yangtze River' : 'China'}

# I used a 'for' loop to iterate through the items (river, country) in the 'rivers' dictionary.
# I printed a statement for each river and its associated country.
for river, country in rivers.items():
    print(f"The {river} runs through the country of {country}")

#I used '\n' just to make space between the outputs making it neater
print('\n')

# I used a 'for' loop to iterate through the keys (river names) in the 'rivers' dictionary.
# I printed each river name.
for river in rivers.keys():
    print(river)

print('\n')

# I used a 'for' loop to iterate through the values (countries) in the 'rivers' dictionary.
for river in rivers.values():
    print(river)
