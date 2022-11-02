"""Reading an Entire file"""
with open('pi_digit.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
print()

"""Reading File line by line"""
file_path = 'pi_digit.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
print()

"""Making a list from the file"""
file_path1 = 'pi_digit.txt'
with open(file_path1) as file_object:
    lines = file_object.readlines()

"""Working with the content"""
pi_string = ''
for line in lines:
    pi_string += line.strip()

# converting the sring into float
print(float(pi_string))
print(f"{pi_string[:20]}...")
print(len(pi_string))
birthday = input("Enter your birthday in a form of mmddyyyy: ")

if birthday in pi_string:
    print("Your birthday is in the pi digits")
else:
    print("Your birthday is not in the pi digits")
