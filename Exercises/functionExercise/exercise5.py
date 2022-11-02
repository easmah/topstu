def sandwiches(*sandwichs):
    """make a list of random arguments"""
    sand = []
    for sandwich in sandwichs:
        sand.append(sandwich)
    return sand


print(sandwiches('chicken', 'beef'))
print(sandwiches('chicken'))
print(sandwiches('chicken', 'cheese', 'pepperoni', 'beef'))


def user_profile(first_name, last_name, **info):
    """Make a dictionary of a user"""
    user = {'firstname': first_name, 'lastname': last_name}

    for key, value in info.items():
        user[key] = value
    return user


user_information= user_profile('Noah', 'Jason', location='sheffield', age='6',school='starter')
print(user_information)


def build_car(make, model, **car_info):
    car_info['make'] = make.title()
    car_info['model'] = model.title()
    return car_info


car = build_car('Honda', 'civic', color='black', tint='tinted', version='sports')
print(car)
