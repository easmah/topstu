"""One advantage of functions is the way they separate blocks of code from your main program.
You can go a step further by storing your functions in a separate file called a module and then importing that module
into your main program. An import statement tells Python to make the code in a module available in the currently
running program file. Storing your functions in a separate file allows you to hide the details of your program’s code
and focus on its higher-level logic. It also allows you to reuse functions in many different programs.
"""


def make_pizzas(size, *toppings):
    print("Making a " + str(size) + " inch pizza, with the following toppings: ")
    for topping in toppings:
        print("\t- " + topping)
