"""
When one class inherits from another, it automatically takes on all the attributes and methods of the first class.
The original class is called the parent class, and the new class is the child class. The child class inherits every
attribute and method from its parent class but is also free to define new attributes and methods of its own.

The first task Python has when creating an instance from a child class is to assign values to all attributes in the
parent class. To do this, the __init__() method for a child class needs help from its parent class.
"""
from classes09.car import Car, Battery


class Electric_Car_in(Car):
    """The super() function is a special function that helps Python make connections between the parent and
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
my_telsa = Electric_Car_in('tesla', 'model s', 2012)
print("\n" + my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.fill_gas_tank()

my_telsa.battery = Battery(900)
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()
