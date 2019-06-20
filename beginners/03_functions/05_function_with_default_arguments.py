'''
Function with default arguments
'''


def hello(message='Welcome to python tutorial'):
    """
     Function with default arguments
    :param message:
    :return:
    """
    print(message)


if __name__ == '__main__':
    # Calling function with argument
    hello('Hello world')

    # Calling function with our argument
    # message formal argument is assigned with default value
    hello()
