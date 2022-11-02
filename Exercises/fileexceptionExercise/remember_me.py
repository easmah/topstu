import json

file_name = 'username_open.json'


def get_new_username():
    username = input("Enter your username: ")
    with open(file_name, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        answer = input(f"Hello, is this the correct username {username} 'y/n': ")
        if answer.lower() == 'y':
            print(f"welcome back {username}")
        else:
            username = get_new_username()
            print(f"We will remember you when you come back {username}")
    else:
        username = get_new_username()
        print(f"We will remember you {username}")


def get_stored_username():
    """Get stored username"""
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


greet_user()