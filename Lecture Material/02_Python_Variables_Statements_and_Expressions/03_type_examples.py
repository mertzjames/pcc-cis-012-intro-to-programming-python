# let's create a simple script that will ask for two inputs and calculate a
# value based on the pythagorian thereom.
a = input("Value for a:")
b = input("Value for b:")

# uncomment this to see what types our inputs are
# print(type(a))
# print(type(b))

# uncomment this to cast the string to an int and thus making this work
# a = int(a)
# b = int(b)

c_squared = a * a + b * b
print("c squared = " + c_squared)
