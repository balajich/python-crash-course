'''
Function with keyword  arguments
'''


def div(a=0, b=1):
    """
    Division function with keyword arguments a,b
    :param a:
    :param b:
    :return:
    """
    return a / b


if __name__ == '__main__':
    # Calling function that has named or keyword arguments
    print(div(10, 2))

    print(div(a=10, b=2))  # Same as above

    print(div(b=2, a=10))  # Same as above order doesnt matter in keyword arguments

    # Calling with default arguments
    print(div())  # Default values are assigned for a & b

    print(div(10))  # Default values are assigned for b
