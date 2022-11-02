for number in range(1, 21):
    print(number)

numbers = list(range(1, 100001))
print(numbers)
print(str(min(numbers)) + " minimum")
print(str(max(numbers)) + " maximum")
print(sum(numbers))

odd_number = list(range(1, 20, 2))
for odd_num in odd_number:
    print(odd_num)

multiple_of_three = [value * 3 for value in range(1, 31)]
print(multiple_of_three)

multiplethree = range(3, 30, 3)
for num in multiplethree:
    print(num)


# List Comprehension
cube = [value ** 3 for value in range(1, 11)]
print(cube)

for value in range(1, 11):
    cubes = value ** 3
    print(cubes)
