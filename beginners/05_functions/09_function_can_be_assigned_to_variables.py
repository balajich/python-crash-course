'''
Assigning 04_functions to varaibles
'''


def add(a, b):
    """
    Function adds two variables
    :param a:
    :param b:
    :return:
    """
    return a + b


if __name__ == '__main__':
    # Calling function with integers as arguments
    print(add(10, 20))

    # assign function to variable sum
    sum = add
    print(sum(10, 20))  # calling the  add function using variable
