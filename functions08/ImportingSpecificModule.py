""" You can also import a specific function from a module. Syntax: from module_name import function_name
You can import as many functions as you want from a module by separating each function’s name with a comma:
from module_name import function_0, function_1, function_2
"""

from storingfunctions_as_modules import make_pizzas

make_pizzas(12, 'pepperoni', 'cheese', 'beef', 'peas')
make_pizzas(6, 'chicken')