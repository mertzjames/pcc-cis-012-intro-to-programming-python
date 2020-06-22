# import json

# # open the file
# # use json.load(file_handler) to extract the data (should be a list or dict)
# # Parse the data 

# with open('Project Material/pokemon_party.json', 'r') as json_reader:
#     data = json.load(json_reader)

#     #print(data[0].get('name'))
#     print(data[0].keys())
#     print(data[0].get('types'))
#     print(data[0].get('weaknesses'))


###### NEW SECTION

# import pokecarddex

# my_dex = pokecarddex.PokeCardDex()
# my_pokemon = pokecarddex.Pokemon(
#     # name
#     # start_hp
#     # ...
# )
# my_dex.add_to_party(my_pokemon)






























class Pokemon():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

pikachu = Pokemon('Pikachu')
mewtwo = Pokemon('Mew Two')

# print(pikachu)
# print(mewtwo) 

class SimpleDex():
    def __init__(self, other_pokemon = None):
        self.party = []
        
        if other_pokemon is not None:
            self.party = other_pokemon

    def add_to_party(self, pokemon):
        self.party.append(pokemon)

    def get_pokemon(self, pokemon_name):
        for pokemon in self.party:
            if pokemon.name == pokemon_name:
                return pokemon

        raise ValueError(f'Pokemon {pokemon_name} is not found!')

my_dex = SimpleDex([pikachu, mewtwo])
my_dex.add_to_party(Pokemon('Bulbasaur'))
print(my_dex.get_pokemon('Mew Two'))



























class FarmAnimal():
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.is_fed = False

    def feed(self):
        self.is_fed = True

    def __str__(self):
        return self.name


class Barn():
    def __init__(self, animals_already_in_barn=None):
        self.tenants = []

        if animals_already_in_barn is not None:
            for animal_name, animal_type in animals_already_in_barn:
                animal = FarmAnimal(animal_name, animal_type)
                self.tenants.append(animal)

    def put_in_barn(self, animal):
        self.tenants.append(animal)

    def take_out_of_barn(self, animal_name):
        for animal in self.tenants:
            if animal.name == animal_name:
                print(f'took out {animal_name}')


    def feed_animals(self):
        for animal in self.tenants:
            animal.feed()


my_barn = Barn([
    ('betty', 'cow'), 
    ('francis', 'horse'), 
    ('joe', 'chicken')
])

print(my_barn.tenants)


sam = FarmAnimal('Sam', 'dog')
my_barn.put_in_barn(sam)

my_barn.take_out_of_barn('betty')

my_barn.feed_animals()



keep_going = True
my_val = 'wanted val'

while keep_going:
    my_val = 'test'
    keep_going = False


print(my_val)

def my_func():
    my_other_val = 'test2'

print(my_other_val)
