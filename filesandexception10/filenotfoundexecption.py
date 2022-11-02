file_name = 'Alice1.txt'

"""with open(file_name, encoding='utf-8') as file_object:
    contents = file_object.read()"""

try:
    with open(file_name, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} was not found")

# Analysing Data
title = 'Alice In Wonderland'
list_text = title.split()
print(list_text)

# Count the number of words in the alice.txt file
file_name_alice = 'alice.txt'


def count_words(file_names):
    try:
        with open(file_names) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry the file {file_names} does not exist")
    else:
        """Count the number of words in the file"""
        content_list = contents.split()
        number_of_words = len(content_list)
        print(f"{file_names.title()} contains: {number_of_words} words.")


count_words(file_name_alice)
print()
list_of_files =['alice.txt', "doesn't_exist.txt", 'little_women.txt']
for filename in list_of_files:
    count_words(filename)


def fail_silently_count_words(name_of_file):
    try:
        with open(name_of_file) as file_objects:
            file_contents = file_objects.read()
    except FileNotFoundError:
        pass
    else:
        """Count the number of words in the file"""
        content_list = file_contents.split()
        number_of_words = len(content_list)
        print(f"{name_of_file.title()} contains: {number_of_words} words.")


print("==== Fail Silently =====")
list_of_files =['alice.txt', "doesn't_exist.txt", 'little_women.txt']
for filename in list_of_files:
    fail_silently_count_words(filename)