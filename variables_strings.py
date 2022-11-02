message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# Strings
# title() converts the first character to upper case AND any uppercase in a word to lower
name = "ada LoveLace money"
print(name.title())
print(name.lower())
print(name.upper())

# Concatenating Strings
first_name = "James"
last_name = "manstrong"
full_name = first_name + " " + last_name
print(full_name)
print("Hello " + full_name.title() + "!")

message = "Hello " + full_name.title() + "!"
print(message)

print("Languages: \n\tPython\n\tJava\n\tJavascript")

# Stripping extra white spaces on the left lstrip()or right rstrip()
favourite_language = "python "
favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language = " JavaScript"
favourite_language = favourite_language.lstrip()
print(favourite_language)

favourite_language = "  nodejs  "
favourite_language = favourite_language.strip()
print("Stripped: " + favourite_language)