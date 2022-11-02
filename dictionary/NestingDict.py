alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print("===============")
for alien in aliens:
    print(alien)
print("===============")

aliens = []
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = ' medium'

for alien in aliens[:5]:
    print(alien)

print("The total number of aliens: " + str(len(aliens)))

# List in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['cheese', 'peperoni', 'chicken']
}
print("You order a pizza with: " + pizza['crust'] + "the following topping: ")
for topping in pizza['toppings']:
    print("\t* " + topping)

print(pizza['toppings'][1])

favourite_language = {
    'jane': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'mike': ['python', 'java', 'c#']
}

for name, languages in favourite_language.items():
    print("\n" + name.title() + "'s favourite languages are: ")
    for language in languages:
        print("\t" + language.title())

# Dictionary in a dictionary
# You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'maria',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print("Username: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFullName: " + full_name.title())
    print("\tLocation: " + location.title())
