

class Pokemon():
    def __init__(self, name, level, start_hp, poke_type):
        self.name = name
        self.level = level
        self.start_hp = start_hp
        self.poke_type = poke_type




class Pokemon():
    def __init__(self, name, level, start_hp, poke_type, move_list):
        self.name = name
        self.level = level
        self.start_hp = start_hp
        self.poke_type = poke_type
        self.move_list = move_list


# Complete example below

class Move():
    def __init__(self, name, power):
        self.name = name
        self.power = power
    

class Pokemon():
    def __init__(self, name, level, start_hp, poke_type, move_list):
        self.name = name
        self.level = level
        self.start_hp = start_hp
        self.poke_type = poke_type
        self.move_list = move_list