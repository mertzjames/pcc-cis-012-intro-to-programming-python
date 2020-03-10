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
