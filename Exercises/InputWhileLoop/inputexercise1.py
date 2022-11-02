prompt = "What car will you like to rent: "
rental_car = input(prompt)

print(f"Let me see if I can find you a {rental_car.title()}")
print()
prompt = "How many seat would you need: "
seating = input(prompt)
seating = int(seating)

if seating > 8:
    print(f"You have to wait for a table")
else:
    print(f"Table is ready")
print()

multiple_of_ten = input("Enter a number: ")
multiple_of_ten = int(multiple_of_ten)
if multiple_of_ten % 10 == 0:
    print(f"{multiple_of_ten} is a multiple of 10")
else:
    print(f"{multiple_of_ten} is not a multiple of 10")
