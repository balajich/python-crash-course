'''
Tuples are immutable lists
'''

if __name__ == "__main__":
    # Create tuple
    t = (1, 2, 3)

    # access element by index
    # Like lists they also start with zero index
    print(t[0])

    # iterate like list
    for e in t:
        print(e)

    # size or number of elements in tuple
    print(len(t))
