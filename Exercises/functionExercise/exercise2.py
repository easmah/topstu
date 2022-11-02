def make_shirt(size, message):
    print(f"The size of the shirt is {size}, and the message to be printed is {message}")


make_shirt(12, 'I love the world')
make_shirt(size=15, message="We are the world!!!!")


def large_shirt(size='large', message='I love Python'):
    print(f"The size of the shirt is {size}, and the message to be printed is {message}")


large_shirt()
large_shirt('Medium')
large_shirt('Large', 'I really love Python')


def describe_city(name_of_city, country='Ghana'):
    print(f"{name_of_city} is in {country}")


describe_city('Accra')
describe_city('Lagos', 'Nigeria')
describe_city('London', 'Uk')
