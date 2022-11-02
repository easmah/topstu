"""if statement allows you to examine the current state of a program and respond appropriately
to that state."""

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("Hold the anchovies")

age = 18
print(age == 18)
print(age > 21)
print(age < 21)
print(age >= 21)
print(age <= 21)

age_0 = 22
age_1 = 18

print()
if age_0 >= 21 and age_1 >= 21:
    print(True)
else:
    print(False)

if age_0 >= 21 or age_1 >= 21:
    print(True)
else:
    print(False)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again")

# Checking if a value is in a list
if 'toyita' in cars:
    print("Found")
else:
    print("not found")

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david', 'james']
user = 'maria'
if user not in banned_users:
    print(user.title() + ", You can post a response if you wish")

print("===== More IF ====")
voting_age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# If-Else Statement
print()
age = 17
if age >= 18:
    print("You are old enough to veto!")
    print("Have you are registered to vote yet")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# If-ELIF-IF
if age < 4:
    print("Your admissioncost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")

print("======= printing now ======")
new_age = 64
if new_age < 4:
    price = 0
elif new_age < 18:
    price = 5
elif new_age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

print("\n==== Testing multiple Conditions ===")
toppings = ['Mushroom', 'cheese', 'tomatoes']
if 'mushroom' in toppings:
    print("Adding mushrooms")
if 'pepperoni' in toppings:
    print("Adding pepperoni")
if 'cheese' in toppings:
    print("Adding cheese")

print("Finished making pizza")

new_pizza_toppings_order = ['mushroom', 'green peppers', 'extra cheese']
for toppings_order in new_pizza_toppings_order:
    if toppings_order == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding "+ toppings_order)

print()
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+ requested_topping + ". ")
    print("Finised making pizza")
else:
    print("Are you sure you want a plain pizza")

available_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'cheese']
toppings_requested = ['mushroom', 'french fries', 'cheese']

for topping in toppings_requested:
    if topping in available_toppings:
        print("Adding "+ topping)
    else:
        print("Sorry, we don't have "+ topping+ ".")

print("Finished making pizza")

users = ['Eric', 'admin', 'james', 'jason', 'noah']
for userr in users:
    if userr == 'admin':
        print("Hello "+userr + ", would you like to see a status report")
    else:
        print("Hello "+ userr + ", thank you for logging in again")

print("======== Blank users ======")
users = []
if users:
    for userr in users:
        if userr == 'admin':
            print("Hello "+userr + ", would you like to see a status report")
        else:
            print("Hello "+ userr + ", thank you for logging in again")
else:
    print("list is blank")

print("\n====== Unique users ======")
usernames = ['Jason', 'Noah', 'Monica', 'Nana', 'Yaa']
new_users = ['Michael', 'Jason', 'NOAH', 'James']

for new_user in new_users:
    if new_user.title() in usernames:
        print("Enter a new user: "+ new_user + " already taken")
    else:
        print("The username: "+ new_user + ", is available")