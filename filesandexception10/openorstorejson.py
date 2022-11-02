import json


def greet_user():
    file_name = 'username_open.json'

    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        pass
    else:
        return username


def get_stored_username():
    username = greet_user()
    if username:
        print(f"Welcome back {username}")
    else:
        file_name = 'username_open.json'
        username = input("Enter your name: ")
        with open(file_name, 'w') as file_object:
            json.dump(username, file_object)
            print(f"We will remember you {username}")


get_stored_username()
