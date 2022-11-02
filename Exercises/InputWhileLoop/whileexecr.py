active = True
toppings_list = []

while active:
    print("Enter quit to exist program")
    toppings = input("Enter your pizza toppings: ")

    if toppings == 'quit':
        active = False
    else:
        print(f"Ading {toppings} to pizza")
        toppings_list.append(toppings)

print(toppings_list)

pizza = []
while True:
    prompt = "Enter pizza topping : [Enter quit to exit program]: "
    pizza_toppings = input(prompt)
    if pizza_toppings =='quit':
        break
    else:
        print(f"adding to {pizza_toppings}")
        pizza.append(pizza_toppings)
print(pizza)



while True:
    prompt = "Enter your age: "
    movie_tickets_age = input(prompt)
    movie_tickets_age = int(movie_tickets_age)

    if movie_tickets_age < 3:
        price = 0
    elif movie_tickets_age <= 12:
        price = 12
    else:
        price = 15
    print(f"The price for the ticket is {price}")