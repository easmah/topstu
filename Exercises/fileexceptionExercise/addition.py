"""Adding numbers"""
prompt = "Enter two numbers: "

while True:
    try:
        first_number = input("Enter the first number: ")
        first_number = int(first_number)
        second_number = input("Enter the second number: ")
        second_number = int(second_number)
    except ValueError:
        print("Sorry, invalid input\n")
    else:
        answer = first_number + second_number
        print(f"The sum of {first_number} and {second_number} is {answer}.\n")

