"""Slicning a list"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[1:])
print(players[-3:])

#Looping through a Slice
for player in players[:3]:
    print(player.title())


#Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
my_foods.append("rice cake")
friends_foods.append('waakye')
print("My favorite foods are: ")
print(my_foods)
print("My friend's favourite foods are ")
print(friends_foods)

for food in my_foods:
    print(food.title())