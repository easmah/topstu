magicians = ['thommy', 'ernest', 'kofi', 'isaac', 'monica', 'Jason', 'noah']


def show_magicians(magicians_names):
    """Passing a list to a function"""
    for magician in magicians_names:
        print(f'{magician.title()} great show tonight')


def make_great(magician):
    for magic in range(len(magician)):
        magicians[magic] = 'Great '+magician[magic]


def make_great_copy(magician):
    while magician:
        current_magician = "Great "+ magician.pop()
        copy_magicians.append(current_magician)


make_great(magicians)
show_magicians(magicians)
print()
print("=================")
magicians = ['thommy', 'ernest', 'kofi', 'isaac', 'monica']
copy_magicians = []
make_great_copy(magicians[:])
show_magicians(copy_magicians)
print()
show_magicians(magicians)
