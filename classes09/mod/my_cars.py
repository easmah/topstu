# Importing Multiple Classes from a Module

from classes09.mod.car import Car, ElectricCar

my_old_car = Car('VW', 'bettle', 2012)
print(my_old_car.get_descriptive_name())

print()
my_new_car = ElectricCar('Ford', 'Focus', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.battery.describe_battery()
