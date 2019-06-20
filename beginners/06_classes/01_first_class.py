'''
Everything is object in python
'''

def fun():
    print('Hello func')
if __name__ == "__main__":
    # Primitives are object
    # int is object
    print(type(10))

    # float is object
    print(type(10.5))

    # boolean is object
    print(type(True))

    # None is object
    print(type(None))

    # Strings are object
    print(type('Hello'))

    # list is object
    print(type([1, 2, 3]))

    # tuple is object
    print(type((1, 2, 3)))

    # set is object
    print(type({1, 2, 3}))

    # dict is object
    print(type({1: 'Alex', 2: 'Nelly', 3: 'Simon'}))

    # lambad is also object
    print(type(lambda x: print(x)))

    # even modules are objects
    import sys

    print(type(sys))
