'''
lambdas can also be passed as functional arguments
'''


def new_add(add, a, b, c):
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
    # create anonymous function  and pass it to function new_add
    print(new_add((lambda a, b: a + b), 10, 20, 30))
