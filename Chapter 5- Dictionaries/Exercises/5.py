# Create dictionaries for different pets, each containing the kind of animal and owner's name.
pet1 = {'animal': 'Dog', 'owner': 'Yuri'}
pet2 = {'animal': 'Cat', 'owner': 'Cerek'}
pet3 = {'animal': 'Bird', 'owner': 'jericc'}
pet4 = {'animal': 'Goldfish', 'owner': 'pat'}

# Store the pet dictionaries in a list called 'pets'.
pets = [pet1, pet2, pet3, pet4]

# Loop through the 'pets' list and print information about each pet.
for pet in pets:
    kind_of_animal = pet['animal']
    owner_name = pet['owner']
    print(f"The pet is a {kind_of_animal} owned by {owner_name}.")


