import json
import datetime
import pathlib
import random

def grab_random_pokemon(mast_list_path, party_list_path):
    mast_path = pathlib.Path(mast_list_path)
    party_path = pathlib.Path(party_list_path)
    with open(mast_path, 'r') as reader, open(party_path, 'w') as writer:
        pokemon = json.load(reader)
        rand_num_in_party = random.randint(5, 10)
        rand_pokemon = [random.choice(pokemon) for i in range(rand_num_in_party)]
        json.dump(rand_pokemon, writer, sort_keys=True, indent=2)

if __name__ == '__main__':
    master_list_path = 'pokemon_master_list.json'
    party_list_path = f'pokemon_party_{datetime.datetime.now()}'
    grab_random_pokemon(master_list_path, party_list_path)
