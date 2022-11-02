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

    def fill_gas_tank(self):
        print("Fill the gas tank till full")


audi_q7 = Car('Audi', 'Q7', 2022)
print(audi_q7.get_descriptive_name())
audi_q7.read_odometer()

# Changing odometer_reading value
print()
audi_q7.odometer_reading = 1000
audi_q7.read_odometer()
audi_q7.fill_gas_tank()

# Accessing through method
audi_q7.update_odometer(2300)
audi_q7.read_odometer()
audi_q7.increment_odometer(1000)
audi_q7.read_odometer()


# Instances as Attributes
class Battery:
    """For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many
    attributes and methods specific to the car’s battery. When we see this happening, we can stop and move those
    attributes and methods to a separate class called Battery. Then we can use a Battery instance as an attribute in
    the ElectricCar class:"""

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




# Inheritance
class ElectricCar(Car):
    """The super() function atxis a special function that helps Python make connections between the parent and
    child class. The name super comes from a convention of calling the parent class a superclass and the child class
    a subclass."""

    # Represents aspects of a car, specifically electric car
    def __init__(self, make, model, year):
        # Initialize attributes of the parent class
        super().__init__(make, model, year)
        # Initializing attributes specific to an electric car
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric car don't need gas tanks"""
        print("This car does not need a gas tank")


"""Overriding Methods from the Parent Class
You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.
To do this, you define a method in the child class with the same name as the method you want to override in the parent
class. Python will disregard the parent class method and only pay attention to the method you define in the
child class"""

my_telsa = ElectricCar('tesla', 'model h', 2019)
print("\n" + my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.fill_gas_tank()

my_telsa.battery = Battery(900)
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()
