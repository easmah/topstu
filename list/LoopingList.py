"""Looping allows you to take the same action, or set of actions, with every item in a list."""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that  was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you magicians. That was a great show!")

for value in range(1, 6):
    print(value)

numbers = list(range(1, 11))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ]
print(min(digits))
print(max(digits))
print(sum(digits))

""" List Comprehension """
squares = [value **2 for value in range(1, 11)]
print(squares)

counting = [value for value in range(1, 21)]
print(counting)

odd_numbers = []
for value in range(1, 20):
    if value % 2 != 0:
        odd_numbers.append(value)
print(odd_numbers)

multiple_three = []
for number in range(1, 31):
    value = number * 3
    multiple_three.append(value)
print(multiple_three)

cubes = []
for value in range(1,11):
    cubes.append(value **3)
print(cubes)

cubes_comp = [value **3 for value in range(1, 10)]
print(cubes_comp)