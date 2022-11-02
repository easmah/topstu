def city_country(name_of_city, country):
    return f'"{name_of_city.title()}, {country.title()}"'


capital = city_country('Accra', 'Ghana')
print(capital)
print(city_country('london', 'United kingdom'))
print(city_country('hambury', 'Germany'))


def make_album(artist, title, songs=None):
    """ Return an album dictionary """
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album


print(make_album("Kendrick Lamar", "Issues", "30"))
print(make_album("The Beatles", "Let It Be", 12))
print(make_album("Michael Jackson", "Thriller"))


def get_album():
    while True:
        print("\nEnter album information")
        print("Enter 'q to quit program")

        artist = input("Artist name: ")
        if artist == 'q':
            break

        title = input("Album title: ")
        if title == 'q':
            break

        song = input("Song number (Optional): ")
        if song == 'q':
            break

        album = make_album(artist, title, song)
        print(album)


get_album()
