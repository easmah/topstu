person0 = {'first_name': 'emmannuel', 'last_name': 'testing', 'age': 20, 'city': 'london'}
person1 = {'first_name': 'noah', 'last_name': 'Lovedr', 'age': 13, 'city': 'Sheffield'}
person2 = {'first_name': 'jason', 'last_name': 'mon', 'age': 21, 'city': 'Accra'}

people = [person0, person1, person2]
for person in people:
    for k, v in person.items():
        print(f'{k} : {v}')
    print()

pet0 = {'animal': 'dog', 'owner': 'bob'}
pet1 = {'animal': 'cat', 'owner': 'noah'}
pet2 = {'animal': 'hamster', 'owner': 'jason'}

pets = [pet0, pet1, pet2]

for pet in pets:
    print(f"The pet is a {pet['animal']} and the owner is {pet['owner'].title()}")

favourite_places = {
    'peter': ['accra', 'lisbon', 'london'],
    'king': ['london', 'barcelona', 'paris']
}

for name, places in favourite_places.items():
    print(f"{name.title()}'s favourite places are: ")
    for place in places:
        print(f"\t- {place}")
    print()

favourite_number = {
    'peter': [9, 10, 8],
    'james': [5, 6, 4],
    'matt': [3, 2],
    'lisa': [8, 5, 3],
    'logan': [6, 9, 11]
}

for name, numbers in favourite_number.items():
    print(f"{name.title()}'s favourite number is: ")
    for number in numbers:
        print(f"\t- {number}")

cities = {
    'new york': {'country': 'US', 'population': '1.2 billion', 'fact': 'More than 800 languages spoken in NYC'},
    'london': {'country': 'UK', 'population': '700 million', 'fact': 'capital is London'},
}

for city, info in cities.items():
    print(f"The city: {city} is located in {info['country']}, with a population of {info['population']}")
    print(f"\t - fact about {city}: {info['fact']}")
