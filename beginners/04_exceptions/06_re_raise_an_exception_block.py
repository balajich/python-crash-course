'''
Raise a new exception
'''


def div(a, b):
    '''
     Divide two numbers
    :param a:
    :param b:
    :return:
    '''
    try:
        result = a / b
    except ZeroDivisionError as e:
        raise ValueError()
    return result


if __name__ == "__main__":
    # Division
    print(div(10, 5))

    # Generates value error
    print(div(10, 0))
