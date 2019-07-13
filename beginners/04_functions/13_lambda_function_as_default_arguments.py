'''
lambdas function as default argument
'''


def new_add(a, b, c, add=(lambda a, b: a + b)):
    '''
    Lambad function will be passed as argument
    :param add:
    :param a:
    :param b:
    :param c:
    :return:
    '''
    return add(a, b) + c


if __name__ == '__main__':
    # lambda function as default argument
    print(new_add(10, 20, 30))

    # Create a lambda function and pass as argument
    print(new_add(10, 20, 30, (lambda a, b: a - b)))
