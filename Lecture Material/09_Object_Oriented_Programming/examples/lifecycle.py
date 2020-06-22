"""
This script is a basic look at the lifecycle of a Python class.  A python class
has 4 main stages:

1. Definition
2. Initialization
3. Access and Manipulation
4. Destruction
"""
print('script start')

class basic():
    print('Stage 1: class definition start')

    prop1 = 1

    def __init__(self):
        print('class basic __init__')
        self.prop2 = 2

    def my_method(self):
        print('class basic my_method')
        return(self.prop1, self.prop2)

    @classmethod
    def cls_method(cls):
        print('class basic cls_method')
        return(cls.prop1)

    def __del__(self):
        print('class basic __del__')

    print('Stage 1: class definition end')

print('class access and manipulation start')
print(basic.prop1)
print(basic.cls_method())
print('class access and manipulation end')

print('Stage 2: object creation start')
b = basic()
c = basic()
print('Stage 2: object creatin end')

print('Stage 3: object access and manipulation start')
print(b.my_method())
print(b.prop2)
print(b.my_method())
print('Stage 3: object access and manipulation end')

print('Stage 4: object destruction start')
del(b)
c = 12
print('Stage 4: object destruction end')

print('script end')
