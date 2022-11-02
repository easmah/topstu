# Returning a Dictionary

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


user = build_person('Monica', 'Richardson')
print(user)


def build_person(firstname, last_name, age=''):
    person = {'first': firstname, 'last': last_name}

    if age:
        person['age'] = age

    return person


person1 = build_person("Emmanuel", "Asmah")
print(person1)

person2 = build_person('Noah', 'Asmah', '5')
print(person2)


# Passing a list
def greet_user(names):
    for name in names:
        message = "Hello " + name.title()
        print(message)


greet_user(['James', 'noah', 'jason', 'mike'])
usernames = ['Life', 'hurt', 'music', 'dance','pope']
greet_user(usernames)


# Modifying a List in a Function
# Start with some designs that need to be printed.
def print_models(unprinted_designs, completed_models):
    """EmmanuelAsmahCV.docx
    Simulate printing each design, until none are left. Move each design to completed_models after printing. """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot', 'dodecahedron', 'tree']
completed_models = []

# Preventing a Function from Modifying a List we use the [:] to make a copy
# print_models(unprinted_designs[:], completed_models)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

"""Passing an arbitrary number of arguments
Sometimes you won’t know ahead of time how many arguments a function needs to accept."""


def make_pizza(*toppings):
    """Print the list of toppings that as been requested
    The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever
    values it receives into this tuple. """
    for topping in toppings:
        print("- " + topping)


make_pizza('Pepperoni')
make_pizza('cheese', 'pepper', 'tomatoes', 'chicken')

"""Mixing Positional and Arbitrary Arguments
If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number 
of arguments must be placed last in the function definition."""


def make_pizzaz(size, *toppings):
    print("Making a " + str(size) + " inch pizza, with the following toppings: ")
    for topping in toppings:
        print("\t- " + topping)


make_pizzaz(12, 'Pepperoni')
make_pizzaz(14, 'mushroom', 'cheese', 'beef', 'green pepper')

"""Using Arbitrary Keyword Arguments
Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of 
information will be passed to the function. In this case, you can write functions that accept as many key-value pairs 
as the calling statement provides. One example involves building user profiles: you know you’ll get information about a 
user, but you’re not sure what kind of information you’ll receive."""


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {'first_name': first, 'last_name': last}

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Noah', 'Jason', location = 'Asaman', region = 'Eastern', age =20)
print(user_profile)
