pizza_names = ['pepperoni pizza', 'texas barbeque', 'chicken supreme', 'American supreme', 'pizza omle']

# copy pizza_names to friend_pizza
friend_pizza = pizza_names[:]
friend_pizza.append('pit pizza')
pizza_names.append('pineapple pizza')

for pizza in pizza_names:
    print("I like " + pizza.title())

print("I really love pizza!")

# Using slice to print first 3
for pizzas in pizza_names[:3]:
    print("The first three pizzas are: " + pizzas)

for middle_pizzas in pizza_names[2:]:
    print("The middle of the list: " + middle_pizzas)

for last_three_pizza in pizza_names[-3:]:
    print("Last pizzas are: " + last_three_pizza)
print("Friends pizza: ")
print(friend_pizza)
print("Pizza names: ")
print(pizza_names)
