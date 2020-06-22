class Pokemon():
    """A class to represent a Pokemon

    Attributes
    ----------
    name : str
        the name of the pokemon
    level : int
        the pokemon level
    hp : int
        the current HP level of the pokemon
    # """
    generation = 'base'

    def __init__(self, name, level, start_hp, energy_type, moves):
        self.name = name
        self.level = level
        self.hp = start_hp
        self.energy_type = energy_type
        self.moves = moves

    def take_damage(self, damage_amount):
        self.hp = self.hp - damage_amount

    def __str__(self):
        return f'Pokemon: {self.name} with {self.hp} HP left'

class WaterPokemon(Pokemon):
    def __init__(self, name:str, level:int, start_hp:int, moves:tuple):
        super().__init__(name, level, start_hp, 'water', moves)
        self.energy_type = 'post_water'


poliwag = WaterPokemon('Poliwag', 13, 60, ('Water Gun', 30))
starmie = WaterPokemon('Starmie', 28, 90, ('Star Freeze', 30))

print(poliwag.energy_type)

# def battle(poke1, poke2):
#     while poke1.hp > 0 and poke2.hp > 0:
#         poke1.take_damage(poke2.moves[1])
#         poke2.take_damage(poke1.moves[1])

#     print(poke1)
#     print(poke2)

# battle(poliwag, starmie)

def my_func(var1: int, var2:str) -> str:
    return var2 * var1
