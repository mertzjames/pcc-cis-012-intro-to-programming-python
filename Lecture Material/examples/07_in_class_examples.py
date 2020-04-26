my_vals = [623, '43', 324.523, '23', '23.23', 234, '342']

def add(values):
    '''take a list of values and adds them up


    We assume that the contents of the list is either int, float or str
    where strings are numbers that can be converted to an int/float

    Parameters
    ----------
    values : list (any)
        a list that represents values to add (can be int, float, or str)

    Returns
    -------
    float
        the sum of all the values'''

    list_of_numbers = []
    for val in values:
        number = float(val)
        list_of_numbers.append(number)

    sum_of_vals = sum(list_of_numbers)
    return sum_of_vals

sum_of_vals = add(my_vals)
print(sum_of_vals)

# Celsius to F 
# celsius x 9 / 5 + 32

cur_temp = 14

def cel_to_f(temp_c):
    temp_f = temp_c * 9/5 + 32
    return temp_f

temp_f = cel_to_f(cur_temp)
print(temp_f)

# F to C
# (F - 32) * 5 / 9
def f_to_cel(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    return temp_c

temp_c = f_to_cel(temp_f)
print(temp_c)



pokedex = {
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

def pokemon_info(index_number):
    '''prints out the pokemon info

    Pokemon at <index> is called <name> with a type of <type>
    '''
