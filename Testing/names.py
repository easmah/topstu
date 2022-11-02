from Testing.name_function import get_formatted_name

print("Enter 'q at anything to quit")
while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break
    last = input("Enter your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted Full name {formatted_name}")
