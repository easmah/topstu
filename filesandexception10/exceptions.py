# ZeroDivisionError
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Sorry, you can not divide by 0")

print("Error handled program running")

# Using Exceptions to prevent Crash
print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Sorry, you can not divide by 0")
    else:
        print(answer)
