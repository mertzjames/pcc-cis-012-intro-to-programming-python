import unittest
import pathlib
import random
import sys

from pokecarddex import Pokemon, PokeCardDex

class TestPokemon(unittest.TestCase):
    def test_initAndAttrs(self):
        p = Pokemon('Charmander', 30, 'fire', 'water', None, (('flamethrower', 25),))
        required_attributes = ['name', 'hp', 'energy_type', 'weakness', 'resiliance', 'moves', 'is_fainted']
        for attr in required_attributes:
            self.assertIn(attr, dir(p))

        self.assertEqual(p.name, 'Charmander')
        self.assertEqual(p.hp, 30)
        self.assertEqual(p.energy_type, 'fire')


class TestPokeCardDex(unittest.TestCase):
    def test_initAndAttrs(self):
        required_attributes = ['party', 'set_order', 'battle', 'heal_party', 'add_to_party']

        card_dex = PokeCardDex()
        for req_attr in required_attributes:
            self.assertIn(req_attr, dir(card_dex))

    def test_initWithJson(self):
        path = pathlib.Path('tests/myParty.json')
        card_dex = PokeCardDex(path.absolute())

        poke_names = [
            'Skarmory',
            'Mareep',
            'Chansey',
            'Machoke',
            'Chikorita',
            'Doduo',
            'Clefable',
            'Persian',
            'Weezing',
        ]

        self.assertEqual(len(poke_names), len(card_dex.party))

        for pokemon in card_dex.party:
            self.assertIn(pokemon.name, poke_names)

    def test_addPokemon(self):
        card_dex = PokeCardDex()

        pokemon = Pokemon('Charmander', 30, 'fire', 'water', None, (('flamethrower', 25),))
        card_dex.add_to_party(pokemon)

        self.assertEqual(card_dex.party[0].name, 'Charmander')
        self.assertEqual(card_dex.party[0].hp, 30)
        self.assertEqual(card_dex.party[0].energy_type, 'fire')

    def test_setOrder(self):
        path = pathlib.Path('tests/myParty.json')
        card_dex = PokeCardDex(path.absolute())

        name_order = [
            'Chikorita',
            'Doduo',
            'Skarmory',
            'Clefable',
            'Weezing',
            'Mareep',
            'Machoke',
            'Persian',
            'Chansey',
        ]

        card_dex.set_order(name_order)
        for name, poke in zip(name_order, card_dex.party):
            self.assertEqual(name, poke.name)

    def test_healPokemon(self):
        path = pathlib.Path('tests/myParty.json')
        card_dex = PokeCardDex(path.absolute())

        expected_hp = [
            60,
            40,
            90,
            80,
            40,
            50,
            70,
            70,
            80
        ]

        for poke in card_dex.party:
              poke.hp = 15

        card_dex.heal_party()

        for hp, poke in zip(expected_hp, card_dex.party):
            self.assertEqual(hp, poke.hp)

    def test_battle(self):
        my_path = pathlib.Path('tests/myParty.json')
        rival_path = pathlib.Path('tests/rivalParty.json')

        my_dex = PokeCardDex(my_path)
        rival_dex = PokeCardDex(rival_path)

        my_dex.battle(rival_dex)

        expected_results_my_dex = [
            ('Skarmory', 0, True),
            ('Mareep', 0, True),
            ('Chansey', 0, True),
            ('Machoke', 0, True),
            ('Chikorita', 0, True),
            ('Doduo', 0, True),
            ('Clefable', 0, True),
            ('Persian', 0, True),
            ('Weezing', 0, True),
        ]

        for expected, poke in zip(expected_results_my_dex, my_dex.party):
            name, hp, is_fainted = expected

            self.assertEqual(name, poke.name)
            self.assertEqual(hp, poke.hp)
            self.assertEqual(is_fainted, poke.is_fainted)

        expected_results_rival_dex = [
            ("Hitmonchan", 0, True),
            ("Meganium", 45, False),
            ("Abra", 30, False),
            ("Zapdos", 90, False),
            ("Butterfree", 70, False),
            ("Ekans", 50, False),
            ("Porygon", 30, False),
            ("Dewgong", 80, False),
            ("Feraligatr", 120, False),
            ("Venomoth", 70, False)
        ]

        for expected, poke in zip(expected_results_rival_dex, rival_dex.party):
            name, hp, is_fainted = expected

            self.assertEqual(name, poke.name)
            self.assertEqual(hp, poke.hp)
            self.assertEqual(is_fainted, poke.is_fainted)


def get_tests():
    return full_suite()

def full_suite():

    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestPokemon),
        unittest.TestLoader().loadTestsFromTestCase(TestPokeCardDex)
    ])

if __name__ == "__main__":
    unittest.main()
