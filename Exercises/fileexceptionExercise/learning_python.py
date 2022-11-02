file_path = 'learning_python.txt'

print("==== Print the contents once by reading in the entire file ====")
with open(file_path) as file_object:
    line = file_object.read()
    print(line.rstrip())

print("\n===== once by looping over the file object =====")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n==== once by storing the lines in a list ====")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('love', 'enjoy')
    print(line.rstrip())