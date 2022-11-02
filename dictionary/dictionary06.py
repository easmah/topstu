"""A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key
to access the value associated with that key. A dictionary is wrapped in braces, {}. Dictionaries are dynamic
structures, and you can add new key-value pairs to a dictionary at any time"""

alien_0 = {'color': 'green', 'points': 5}

# Accessing values in a Dictionary
print(alien_0['color'])
print("You have earned " + str(alien_0['points']) + " points")

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(alien_0)

# Modifying values in Dictionary
alien_0['color'] = 'yellow'
print(alien_0)

# Move the alien t the right
# Determine ow far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# Removing Key-Value Pairs
del alien_0['points']
print(alien_0)

#
favourite_language = {
    'jen': 'pyhton',
    'james': 'c',
    'noah': 'java',
    'jason': 'python'
}
print()
for name, language in favourite_language.items():
    print(name.title() + "' favourite language is: " + language.title())
print()

# Looping Through All the Keys in a Dictionary
for name in favourite_language.keys():
    print(name.title())
print()

print("Jason's favourite language is: " + favourite_language['jason'].title())

person = {
    'firstname': 'Jason',
    'lastname': 'Tomas',
    'age': 32,
    'city': 'Accra'
}

print("firstname: " + person['firstname'])
print("lastname: " + person['lastname'])
print("age: " + str(person['age']))

# Looping through Dictionary
print("Looping through")
for key, value in person.items():
    print(key, value)

friends = ['James', 'Jason']
for name in favourite_language.keys():
    if name.title() in friends:
        print("Hi " + name.title() + ", your favourite language is: " + favourite_language[name].title())
    else:
        print("Name "+ name.title() + " is not in friends")

print()
# Sorted dictionary
for name in sorted(favourite_language.keys()):
    print(name.title())

# Looping Through All Values in a Dictionary
print()
print("The following program has found")
for language in favourite_language.values():
    print(language.title())
