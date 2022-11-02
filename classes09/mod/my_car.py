# Importing a Single Class
"""The import statement tells Python to open the car module and import the class Car. Now we can use the Car class
as if it were defined in this file."""

from classes09.mod.car import Car

my_new_car = Car("Honda", "Civic", 2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()