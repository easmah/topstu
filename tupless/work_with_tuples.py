"""Lists work well for storing sets of items that can change throughout the
life of a program. However, sometimes you’ll want to create a list of items that cannot
change. Tuples allow you to do just that. Python refers to values that cannot change as immutable,
and an immutable list is called a tuple.
A tuple looks just like a list except you use parentheses instead of square brackets.
"""

dimensions = (200, 50)
print("Original dimension: ")
print(dimensions)


dimensions = (400, 100)
print("\nModified dimensions: ")
print(dimensions)
