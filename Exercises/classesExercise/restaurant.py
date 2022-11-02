class Restaurant:
    """Simple Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and the Cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open")

    def set_number_served(self, guest):
        self.number_served = guest

    def increment_numbers_served(self, increment):
        self.number_served += increment


# Part 1
my_restaurant = Restaurant('Cocoa', 'African')
print(f"The name is {my_restaurant.restaurant_name}")
print(f"The cuisine is {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

'''#Part 2
papaye = Restaurant('Papaye', 'West African')
brostio = Restaurant('brostio', 'French')
chippie = Restaurant('Chippie', 'English')

papaye.describe_restaurant()
brostio.describe_restaurant()
chippie.describe_restaurant()'''
print("==============")
to_serve = papaye = Restaurant('Papaye', 'West African')
print(to_serve.number_served)
print(f"{to_serve.number_served}")
to_serve.describe_restaurant()
to_serve.set_number_served(10)
print(to_serve.number_served)
to_serve.increment_numbers_served(5)
print(to_serve.number_served)


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print(f"- {flavor}")


flavor_list = ['mongo', 'strawberry', 'apple']
ice_cream = IceCreamStand('Papaye', 'West African', flavor_list)
ice_cream.describe_restaurant()
ice_cream.display_flavors()
