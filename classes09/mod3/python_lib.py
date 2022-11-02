"""Dictionaries allow you to connect pieces of information, but they don’t keep track of the order in which you add
key-value pairs. If you’re creating a dictionary and want to keep track of the order in which key-value pairs are added,
you can use the OrderedDict class from the collections module."""

from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is  " + language.title()+".")

"""We begin by importing the OrderedDict class from the module collections. create an instance of the 
OrderedDict class and store this instance in favorite_languages. Notice there are no curly brackets; the call to 
OrderedDict() creates an empty ordered dictionary for us and stores it in favorite_languages. We then add each name 
and language to favorite_languages one. Now when we loop through favorite_languages, we know we’ll 
always get responses back in the order they were added:"""