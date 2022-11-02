import json

file_name = 'favourite_number.json'

try:
    with open(file_name) as file_obj:
        contents = json.load(file_obj)
except FileNotFoundError:
    user_number = input('Enter your favourite number: ')
    with open(file_name, 'w') as file_object:
        json.dump(user_number, file_object)
        print(f"Your favourite number is {user_number}")
else:
    print(f"I know your favourite number, it's {contents}")