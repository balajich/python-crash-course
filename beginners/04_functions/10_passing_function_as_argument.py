'''
Passing 04_functions are arguments
'''


def add(a, b):
    """
    Function adds two variables
    :param a:
    :param b:
    :return:
    """
    return a + b


def new_add(add, a, b, c):
    '''
    Functions can also be passed as  arguments
    :param add:
    :param a:
    :param b:
    :param c:
    :return:
    '''
    return add(a, b) + c


if __name__ == '__main__':
    # Calling function with integers as arguments
    print(add(10, 20))

    # pass add function as argument
    print(new_add(add, 10, 20, 30))
    # This is also called as decorator pattern
