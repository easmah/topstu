sandwich_orders = ['pastrami','beacon sandwich', 'chicken sandwich','pastrami', 'BLT', 'tuna sandwich', 'pastrami']
finished_sandwich = []
active = True

'''while active:
    for sandwich in sandwich_orders:
        print(f"I made your {sandwich}")
        finished_sandwich.append(sandwich)
        active = False
    print(finished_sandwich)
    print()'''

'''while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")

    finished_sandwich.append(sandwich)
print("---- Finished Sandwich ----")
for sandwich in finished_sandwich:
    print(f"We make a {sandwich}")'''

print()
print(f"Sorry, we ran out of Pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")

    finished_sandwich.append(sandwich)
print("---- Finished Sandwich ----")
for sandwich in finished_sandwich:
    print(f"We make a {sandwich}")


print("\n====================")
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name: ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response

    repeat = input("Would you like to go to another place? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n====== Polling Results ======")
for name, places in responses.items():
    print(f"{name} would like to visit: {places}.")



