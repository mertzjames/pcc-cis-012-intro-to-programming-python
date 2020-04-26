POKEDEX = {
    25: {
        'name': 'Pikachu',
        'type': 'electric'
    },
    1: {
        'name': 'Bulbasaur',
        'type': 'grass'
    },
    4: {
        'name': 'Charmander',
        'type': 'fire'
    }
}


def print_pokemon_info(index_number):
    '''prints out the pokemon info

    Pokemon at <index> is called <name> with a type of <type>
    '''
    pokemon = POKEDEX[index_number]
    name = pokemon.get('name', 'undefined')
    poke_type = pokemon['type']
    print(f'Pokemon at {index_number} is called {name} with a type of {poke_type}')

# for each index in pokedex, info function
for poke_index in POKEDEX.keys():
    print_pokemon_info(poke_index)

# Warren's solution
def print_pokemon(index, name, type):
    print(f'Pokemon at {index} is called {name} with a type of {type}')

for index, pokemon in POKEDEX.items():
    print_pokemon(index, **pokemon)





































def add_pokemon(index, name, poke_type):
    POKEDEX[index] = {
        'name': name,
        'type': poke_type
    }