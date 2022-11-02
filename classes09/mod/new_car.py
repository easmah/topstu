import car

"""
Importing an entire module
You can also import an entire module and then access the classes you need using dot notation. This approach is simple 
and results in code that is easy to read.
"""
my_bettle = car.Car('vW', 'bettle', 2012)
print(my_bettle.get_descriptive_name())

my_electric = car.ElectricCar('Teslas','Model X', 2019)
print(my_electric.get_descriptive_name())



