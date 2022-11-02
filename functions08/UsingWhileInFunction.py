def while_function():
    while True:
        print("Enter your name")
        print("Enter 'q' to quit")
        first_name = input("First name: ")
        if first_name == 'q':
            break

        last_name = input("Last name: ")
        if last_name == 'q':
            break

        print("full name is: " + first_name.title() + ' ' + last_name.title() + "\n")


while_function()
