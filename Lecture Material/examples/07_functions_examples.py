def hello(person):
    '''Says hello and returns the greeting

    Parameters
    ----------
    person : str
        the name of the person that we want to say hello to

    Returns
    -------
    str
        the greeting used to say hello'''

    # notice indentation throughout the body

    # function body
    greeting = f'Hello {person}!'
    print(greeting)

    return greeting

def value_returning():
    return 1

print(value_returning())

def non_value_returning():
    print('Hello World!')

var = non_value_returning()
print(var)