person = {'first_name': 'emmannuel',
          'last_name': 'testing',
          'age': 20,
          'city': 'Sheffield'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

for key, value in person.items():
    print('key: ' + key + " - value: " + str(value))

favourite_number = {
    'peter': 9,
    'james': 5,
    'matt': 3,
    'lisa': 8,
    'logan': 6,
}

print("Peter's favourite number is: " + str(favourite_number['peter']))
print("James's favourite number is: " + str(favourite_number['peter']))
print("Matt's favourite number is: " + str(favourite_number['peter']))
print("Lisa's favourite number is: " + str(favourite_number['peter']))
print("Logan's favourite number is: " + str(favourite_number['peter']))
