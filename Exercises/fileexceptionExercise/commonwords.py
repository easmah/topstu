"""Read the file and print how many times a text appear in the file"""

file_name = 'little_women.txt'

try:
    with open(file_name) as f_object:
        contents = f_object.read()
except FileNotFoundError:
    print(f"File {file_name} not found")
else:
    word_count = contents
    print(word_count.count('This'))
    print(f"To lower: {word_count.count('this'.lower())}")
