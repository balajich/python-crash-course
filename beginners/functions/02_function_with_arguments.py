'''
Function with arguments
'''


def add(a, b):
    """
    Function adds two variables
    :param a:
    :param b:
    :return:
    """
    print(a + b)


if __name__ == '__main__':
    # Calling function with integers as arguments
    add(10, 20)

    # Calling function with floats as arguments
    add(1.5, 2.5)

    # Calling functions with boolean as arguments
    add(True, False)

    # Calling functions with strings as arguments
    # if it is string type, variable are going to be concatenated
    add('Hello', 'World')

    # You cannot add two different types of variables
    # The below call will result an error
    # It can add or concatenate variables belong to same group
    add('Hello', 20)
