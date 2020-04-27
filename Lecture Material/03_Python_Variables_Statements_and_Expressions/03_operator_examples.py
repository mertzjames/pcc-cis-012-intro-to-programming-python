# Let's create a program that will find the remainder of the division of a
# quotient by a divisor.

print("This program will display the remainder of the division between a dividend and divisor")

dividend = int(input("Dividend: "))
divisor = int(input("Divisor: "))

remainder = dividend % divisor

# common mistake
#print("Remainder: " + remainder)

# better
#print("Remainder: " + str(remainder))
# best
print(f'Remainder: {remainder}')

## Let's create a program thit will take two strings and concanenates them

print("Please enter in two random phrases")

phrase_one = input("Phrase One: ")
phrase_two = input("Phrase Two: ")

print(phrase_one + phrase_two)

## some interesting behaviors of variables

# the is operator checks to see if the values come from the same place in memory
# the == operator checks for value equality
a = 4
b = 4
print(f'a, b: {a}, {b}')
print(f"a == b: {a == b}")
print(f"a is b: {a is b}")

# Python does some optimizations to save mem space and preallocates values under
# 256 to point to the same addresses.
a = 2 ** 16
b = 2 ** 16
print(f'a, b: {a}, {b}')
print(f'a == b: {a == b}')
print(f"a is b: {a is b}")
