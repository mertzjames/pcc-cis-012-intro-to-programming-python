"""
PokeCardDex template.  This is a template file that is used to 
"""

class Pokemon():
    def __init__(self, name, start_hp, energy_type, weakness, resistence, moves):
        # The following is a summary of the inputs to this class:
        # - (str) name: the name of the pokemon
        # - (int) start_hp: the starting (or base) hp of the pokemon
        # - (str) energy_type: the energy type of the pokemon (electric, water,
        #   fire, etc,.)
        # - (str) weakness: the energy type the pokemon is weak against
        # - (str) resistence: the energy type the pokemon is resistant against
        # - (tuple) moves: a tuple of ((str), (int)) pairs that represent the
        #   move name and damage amount
        pass


class PokeCardDex():
    def __init__(self, json_file_path=None):
        # NOTE: It is important to handle the case where no path is passed in
        # meaning that json_file_path has a value of None.
        pass

    def set_order(self, order):
        pass

    def battle(self, challenger_party):
        pass

    def heal_party(self):
        pass

    def add_to_party(self, pokemon):
        pass



# Below is an example usage for using the classes
if __name__ == "__main__":
    my_dex = PokeCardDex('pokemon_party.json')
    rival_dex = PokeCardDex()
    pikachu = Pokemon('Pikachu', 100, 'electric', None, None, (('electric charge', 30),))
    rival_dex.add_to_party(pikachu)

    my_dex.battle(rival_dex)

    # for pokemon in my_dex.party:
    #     print(pokemon.is_fainted)

    my_dex.heal_party()
