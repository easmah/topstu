import json

""" Writing/Storing a json with json.dump"""
numbers = [2, 3, 5, 7, 9, 11, 13]
file_name = 'numbers.json'

with open(file_name, 'w') as file_object:
    json.dump(numbers, file_object)

""" Reading a stored json with json.load()"""
with open(file_name) as file_reader:
    numbers = json.load(file_reader)
print(numbers)

""" Taking user input and storing it """
filename = 'username.json'
username = input("Enter your name: ")

with open(filename, 'w') as fileobject:
    json.dump(username, fileobject)
    print(f"we will remember you {username}")

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back {username}")
