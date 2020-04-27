# Exercise 1
pokemon = ('picachu', 'charmander', 'bulbasaur')
print(pokemon)

# Exercise 2
print(pokemon[1])

# Exercise 3
starter1, starter2, starter3 = pokemon
print(starter1)
print(starter2)
print(starter3)

# Exercise 4
my_name = tuple('james mertz')
print(my_name)

# Exercise 5
print('i' in my_name)

# Exercise 6
for i in range(2, 11):
    print(i)

# Exercise 7
i = 2
while i < 11:
    print(f'i = {i}')
    i += 1

# Exercise 8
my_str = "This is a simple string"
for c in my_str:
    print(c)

# Exercise 9
simple_set = ("this", 'is', 'a', 'simple', 'set')
for word in simple_set:
    for i in range(3):
        print(word)

for i in range(3):
    for word in simple_set:
        print(word)


# Here is a quick example of what a for loop helps to reduce
pokemon = ('picachu', 'charmander', 'bulbasaur', 'mew', 'mewtwo')

# the below is what the for loop is doing
monster = pokemon[0]
print(monster)
monster = pokemon[1]
print(monster)
# ....
monster = pokemon[4]
print(monster)

for monster in pokemon:
    print(monster.upper())


# food = ['rice', 'beans']
# print(food)

# food.append('broccoli')
# print(food)

# food.extend(['pizza', 'bread'])
# print(food)

# print(food[0:2])
# print(food[:2])

# print(food[4])
# print(food[len(food) - 1])
# print(food[-1])

# breakfast = 'eggs,fruit,orange juice'.split(',')
# print(breakfast)
# print(len(breakfast))

# # Exercise 8
# numbers = []

# while True:
#     # first we want to prompt the user for an input
#     val = input("Please enter a number: ")

#     # next let's check if the user wants to stop
#     if val == 'stop':
#         # if user says stop, stop
#         break

#     # if not, add user input to list
#     val = float(val)
#     numbers.append(val)

# avg = sum(numbers) / len(numbers)
# min_val = min(numbers)
# max_val = max(numbers)

# print(f"Your avg is {avg}")
# print(f"Your min is {min_val}")
# print(f"Your max is {max_val}")


pokedex = {}
print(pokedex)

pokedex['Venosaur'] = ['Grass', 'Poisen']
pokedex['Charizard'] = ['Fire', 'Flying']
pokedex['Blastoise'] = ['Water']
print(pokedex)
print(pokedex['Venosaur'][0])

del pokedex['Blastoise']
print(pokedex)