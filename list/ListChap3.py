""" A list is a collection of items in a particular order. square brackets ([]) indicate a list.
Lists are ordered collections, so you can access any element in a list by telling the position, or index, of the item desired.
The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value
appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have
been removed.
"""

bicycles = ['tricycle', 'trek', 'cannondale', 'redline', 'specialised']
print(bicycles)
print(bicycles[0])
print(bicycles[2].title())
print(bicycles[-1])
print(bicycles[-2])

message = "My first bicycle is " + bicycles[0] + "."
print(message)

motorcycles = ['Honda', 'Kawasaki', 'Yamaha', 'Suzuki', 'Harley Davis']
print(motorcycles)
motorcycles[3] = 'Ducati'
print(motorcycles)
motorcycles.append('Suzuki')
print(motorcycles)
motorcycles.insert(1, 'Bmw')
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# Removing by value
motorcycles.remove('Honda')
print(motorcycles)
# To remove last word
suzuki_pop = motorcycles.pop()
print(motorcycles)
print(suzuki_pop)
message = 'The las motorcyle I owned was ' + suzuki_pop + '.'
print(message)

removed_kawasaki = 'Kawasaki'
motorcycles.remove(removed_kawasaki)
print(motorcycles)

# Popping from any position
any_pop = motorcycles.pop(1)
print(motorcycles)

print()
names = []
names.append('Noah')
names.append('Jason')
names.append('Emmauel')
print(names)

# Organising a list
names.sort()
print("===============")
print(names)
names.sort(reverse=True)
print(names)
sort_names = sorted(names)
print("======== ")
print(sort_names)
print(sort_names.sort())
print("=========")

print(sorted(names))
print(names)
names.append("Michael")
print("reversing names")
names.reverse()
print(names)

# Finding the length of a list
print(len(names))