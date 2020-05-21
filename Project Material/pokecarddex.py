"""
PokeCardDex template.  This is a template file that is used to 
"""

class Pokemon():
    def __init__(self, name, start_hp, energy_type, weakness, resistence, moves):
        pass


class PokeCardDex():
    def __init__(self, json_file_path=None):
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
