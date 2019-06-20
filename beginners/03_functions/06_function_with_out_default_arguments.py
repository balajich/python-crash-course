'''
Function with out default arguments
'''


def hello(message):
    """
     Function with out default arguments
    :param message:
    :return:
    """
    print(message)


if __name__ == '__main__':
    # Calling function with argument
    hello('Hello world')

    # Calling function with out argument
    # Below call is going fail with error stating positional arguments are mandatory
    hello()
