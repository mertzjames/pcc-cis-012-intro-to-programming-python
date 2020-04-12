# Variables that are intended to never change during execution should be at the
# top of the file and in ALL CAPS.  These are called CONSTANTS.
PI = 3.14
E = 2.71

# Example of good and better Variable Names
s = 3600
seconds = 3600

# multi-worded names should use underscore in between:
phrase = "Mistakes were made."
long_phrase = "There are no winners or losers in the race of life; only finisher and quitters"

# you CAN use unicode, but use a decriptive name instead
Ω = 0.567
OMEGA = 0.567

# Chaining the assignment operator
# BE CAREFUL ABOUT THIS!  You don't want to be confusing.
seconds = minutes = 60

# Example of non-working Variable Names (Uncomment and run to see what happens)
# -bender = "Remember Me!"
# 4turama = 'Only the best show on earth!'
# lel@ = 'one eyed freak'

# What happens when we set a variable to two different values?
prompt = "What is your name?"
prompt = "Where are you?"
print(prompt)

# Take this further and do the following on your own:
# - create variables that represents a name, age, and date of birth and print
#   them out individually.
my_name = "kronos"
age = 23
birthdate = "2 May"
print("my name is:")
print(my_name)
print("my age is:", age)
print("my birthdate is:" + birthdate)