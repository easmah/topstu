file_name = 'guest_book.txt'

active = True
while active:
    prompt = 'Enter some names: '
    prompt += "Enter 'q' to quit: "
    user_name = input(prompt)
    if user_name == 'q':
        print('Quitting now')
        active = False
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(f"{user_name}\n")
