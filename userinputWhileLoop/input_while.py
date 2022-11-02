""" The input() function pauses your program and waits for the user to enter some text. """
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name.title())

# Sometimes you’ll want to write a prompt that’s longer than one line.
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your firstname: "

first_name = input(prompt)
print('Hello, ' + first_name.title())


# Using int(0 to accept input. The int() function converts a string representation of a number to a numerical
# representation
age = input("How old ae you: ")
age = int(age)
print(age)

height = input("How tall are you? ")
height = int(height)
if height >= 36:
    print("You're tall enough to ride")
else:
    print("You'll be able to ride when you're a little older")

# Modulo Operator
""" A useful tool for working with numerical information is the modulo operator (%), which divides one number by 
another number and returns the remainder"""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("Number is " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd")
