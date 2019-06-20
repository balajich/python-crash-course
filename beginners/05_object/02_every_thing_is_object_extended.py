'''
Everything is object in python.
even function ,lambda module ..etc
'''


def fun():
    print('Hello func')


if __name__ == "__main__":
    # lambda is also object
    print(type(lambda x: print(x)))

    # function is also object
    print(type(fun))

    # even modules are objects
    import sys

    print(type(sys))
