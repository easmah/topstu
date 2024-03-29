class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    # Accessing odometer reading directly through method
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer reading")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Instances as Attributes
class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery")

    def get_range(self):

        if self.battery_size <= 70:
            range = 240
        elif self.battery_size > 70:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on full charge"
        print(message)


class ElectricCar(Car):

    # Represents aspects of a car, specifically electric car
    def __init__(self, make, model, year):
        # Initialize attributes of the parent class
        super().__init__(make, model, year)
        # Initializing attributes specific to an electric car
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric car don't need gas tanks"""
        print("This car does not need a gas tank")
