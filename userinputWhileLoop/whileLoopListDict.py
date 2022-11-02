"""Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine
and report on later."""

unconfirmed_users = ['alice', 'brian', 'Kojo']
confirmed_users = []

# verify each user until they are no more unfirmed users
# Move each verified user into list of confirmed

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Displaying all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', 'dog']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a Dictionary with user Input
responses = {}
responses_list = []

# Set a flag to indicated the polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response
    responses_list.append(response)

    # Find out if anyone else is going to to take the poll
    repeat = input("Would anyone else like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

    # Polling is complete. Show the results:
    print("\n --- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")

    print(responses)
    print(responses_list)

