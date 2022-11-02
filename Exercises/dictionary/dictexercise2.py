rivers = {'nile': 'egypt',
          'amazon': 'brazil',
          'volta': 'ghana',
          'yangtse': 'china'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}")

print()
for river in rivers.keys():
    print(river.title())

print()
for country in rivers.values():
    print(country.title())

favourite_languages = {
    'jen': 'python',
    'sarah': 'java',
    'edward': ' ruby',
    'phil': 'python'
}

people = ['jen', 'mike', 'phil', 'noah', 'monica']
for person in people:
    if person in favourite_languages.keys():
        print(f'Thank you for taking the poll: {person}')
    else:
        print(f'Can you please take the poll: {person}')
        