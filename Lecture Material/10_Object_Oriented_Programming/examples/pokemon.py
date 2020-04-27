class EnergyType():
    pass


class Move():
    def __init__(self, name, base_damage):
        self.name = name
        self.base_damage = base_damage
        self.energy_cost = energy_cost

class Pokemon():
    def __init__(self, name, energy_types, move_list):

