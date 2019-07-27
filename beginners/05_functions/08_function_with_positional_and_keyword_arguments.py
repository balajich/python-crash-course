'''
Function with positional and key word arguments
'''


def add(a, b, c=0, d=0):
    """
    Division function with position argumenst a,b and keyword arguments c,d with default values
    :param a:
    :param b:
    :return:
    """
    return a + b + c + d


if __name__ == '__main__':
    # Calling function that has both keyword and named arguments
    print(add(1, 2, c=3, d=4))

    print(add(1, 2, c=3))  # This is OK

    print(add(2, c=3, d=4))  # This is not OK, leads to error
