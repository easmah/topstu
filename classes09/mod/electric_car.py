# Storing Multiple Classes in a Module
from classes09.mod.car import ElectricCar

my_electric_car = ElectricCar('Telsa', 'model z', 2021)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
