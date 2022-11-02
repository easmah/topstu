"""Read the context of files """


def read_files(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
    else:
        print(f"The content of {filename} is \n{contents}")


file_names = ['dogs.txt', 'cats.txt']
for content in file_names:
    read_files(content)


def fail_silently_read_files(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(f"The content of {filename} is \n{contents}")


print("====================")
file_names = ['dogs.txt', 'cats.txt']
for content in file_names:
    fail_silently_read_files(content)