""" When you write a class, you define the general behavior that a whole category of objects can have.
Making an object from a class is called instantiation, and you work with instances of a class
Creating and using a Class dog.py
You can model almost anything using classes. Let’s start by writing a simple class, Dog, that represents a dog—not
one dog in particular, but any dog.
"""
"""
the __init__() Method
The __init__() method is a special method Python runs automatically whenever we create a new instance 
based on the Dog class. The self parameter is required in the method definition, and it must come first before the 
other parameters.
Every method call associated with a class automatically passes self, which
is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the 
class. When we make an instance of Dog, Python will call the __init__() method from the Dog class.
"""


# A simple attempt to model a dog
class Dog:

    def __init__(self, name, age):
        # Initialize name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        # Simulate a dog sitting to a response
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        # Simulate a dog rolling over to a response
        print(self.name.title() + " is rolling over")


""" The __init__() method creates an instance representing this particular dog and sets the name and age attributes 
using the values we provided. The __init__() method has no explicit return statement, but Python automatically returns 
an instance representing this dog. We store that instance in the variable my_dog. 
To access the attributes of an instance, you use dot notation. After we create an instance from the class Dog, 
we can use dot notation to call any method defined in Dog."""
my_dog = Dog('willie', 4)
print("My dog name is " + my_dog.name.title())
print("My dog age is " + str(my_dog.age))
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Span', 2)
print("\nYour dog name is: " + your_dog.name)
print("Your dog age is: " + str(your_dog.age))
your_dog.sit()
your_dog.roll_over()