friends = ['noah', 'jason', 'ernest']

print(friends[0].title())
print(friends[1].title())
print(friends[2].title())

print()
for name in friends:
    print("Hello " + name.title() + ", you are invite to the party")

print(friends[2])

# replace a value
friends[2] = 'monica'
for name in friends:
    print("Hello " + name.title() + ", you are invite to the party")

print("bigger hall found")
friends.insert(0, 'Thommy')
friends.insert(2, 'ernest')
friends.append('kofi')

for name in friends:
    print("Hello " + name.title() + ", you are invite to the new party")

print("Sorry venue is not ready, so only 2 people can come")
print(len(friends))
kofi_last = friends[5]
print(friends.pop() + " can't make it")
print(friends.pop() + " can't make it")
print(friends.pop() + " can't make it")
print(friends.pop() + " can't make it")

print(len(friends))

del friends[:]
print(friends)

