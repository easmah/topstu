file_name = 'programming_poll.txt'

active = True
while active:
    prompt = 'Why to you like programming: '
    prompt += "Enter 'q' to quit: "
    programming = input(prompt)
    if programming == 'q':
        print('Quitting now')
        active = False
    else:
        with open(file_name, 'a') as file_object:
            file_object.write(f"{programming}")