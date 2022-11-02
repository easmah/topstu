"""Functions, which are named blocks of code that are designed to do one specific job. If you need to
perform that task multiple times throughout your program, you don’t need to type all the code for the same task again
and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside
the function. You’ll find that using functions makes your programs easier to write, read, test, and fix."""


def greet_user():
    print("Hello, welcome")


# Calling a function
greet_user()


# Function that accepts a parameter
def greet_user(username):
    print("Hello, " + username + " welcome")


# Passing an argument (Jason and Noah)
greet_user("Jason")
greet_user("Noah")

# Arguments and Parameters
"""The variable username in the definition of greet_user() is an example of a parameter, a piece of information the 
function needs to do its job. The value 'jesse' in greet_user('jesse') is an example of an argument. An argument
is a piece of information that is passed from a function call to a function."""


def favourite_book(title):
    print("My favourite book is: " + title)


favourite_book("The Richest Man Babylon")


# Using a positional argument parameters
def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type)
    print("The name of my " + animal_type + " is: " + pet_name)


describe_pet("dog", "Spooky")

# Using a keyword argument
"""A keyword argument is a name-value pair that you pass to a function. Keyword arguments free you from having to worry 
about correctly ordering your arguments in the function call, and they clarify the role of each value in the 
function call."""
describe_pet(pet_name="Messy", animal_type="dog")
describe_pet(animal_type="Hamster", pet_name="StickyLog")

# Default Values
"""When writing a function, you can define a default value for each parameter. If an argument for a parameter is 
provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.
When you use default values, any parameter with a default value needs to be listed after all the parameters that 
don’t have default values. This allows Python to con- tinue interpreting positional arguments correctly."""


def default_describe_pet(pet_name, animal_type='dog'):
    print("I have a " + animal_type)
    print("The name of my " + animal_type + " is: " + pet_name)


default_describe_pet("Locker")
default_describe_pet(pet_name='SecretOp')
default_describe_pet("lost", 'cat')

# return Values
"""A function doesn’t always have to display its output directly. Instead, it can process some data and then return a 
value or set of values. The value the function returns is called a return value."""


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name("jimmy", "hendricks")
print(musician)

""" Making an Argument Optional
Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra 
information only if they want to."""


def get_user_full_name(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


user = get_user_full_name("Jason", "Noah")
print(user)

user = get_user_full_name("james", "lee", "Noah")
print(user)
