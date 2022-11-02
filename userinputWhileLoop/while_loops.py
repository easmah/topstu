"""The for loop takes a collection of items and executes a block of code once for each item in the collection.
In contrast, the while loop runs as long as, or while, a certain condition is true."""

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1  # The += operator is shorthand for current_number = current_number + 1.

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

"""For a program that should run only as long as many conditions are true, you can define one variable that determines 
whether or not the entire pro- gram is active. This variable, called a flag, acts as a signal to the program. We can 
write our programs so they run while the flag is set to True and stop run- ning when any of several events sets the 
value of the flag to False. """
active = True
while active:
    new_message = input(prompt)
    if new_message == 'quit':
        active = False
    else:
        print(new_message)

# Using break to Exit a Loop
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


"""Using continue in a Loop
Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement 
to return to the beginning of the loop based on the result of a conditional test."""

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)