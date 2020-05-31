import unittest
import sys

def get_tests():
    return full_suite()


def full_suite():

    from tests.test_pokecarddex import TestPokemon, TestPokeCardDex

    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestPokemon),
        unittest.TestLoader().loadTestsFromTestCase(TestPokeCardDex)
    ])

if __name__ == "__main__":
    unittest.main()
