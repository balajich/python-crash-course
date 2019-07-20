'''
Various ways to create list
'''

if __name__ == "__main__":
    # Create list
    l = [1, 2, 3]
    print(l)

    # Unpack list
    x, y, z = l
    print(x, y, z)

    # ignore first element and use rest of element
    _, y, z = l
    print(y, z)
