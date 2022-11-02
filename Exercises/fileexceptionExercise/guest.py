file_name = 'guest.txt'

user_name = input('Enter your name: ')

with open(file_name, 'a') as file_object:
    file_object.write(f"{user_name}\n")
