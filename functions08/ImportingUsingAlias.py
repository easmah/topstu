"""Using as to Give a Function an Alias
If the name of a function you’re importing might conflict with an exist- ing name in your program or if the function
name is long, you can use a short, unique alias—an alternate name similar to a nickname for the func- tion.
"""

from storingfunctions_as_modules import make_pizzas as make

# Using as to Give a Module an Alias
"""You can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call 
the module’s functions more quickly."""
import storingfunctions_as_modules as p


make(5, 'tomatoes', 'cheese', 'chicken')

p.make_pizzas(90, 'Cheese', 'hot dog')


"""Importing All Functions in a Module
You can tell Python to import every function in a module by using the aster- isk (*) operator:
from pizza import * """
