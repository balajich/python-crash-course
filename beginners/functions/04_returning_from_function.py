'''
Understanding Return statement
'''


def div(a, b):
    """
     Division function. When divisor (b) is passed as zero. We will return None
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return
    else:
        return a / b


if __name__ == '__main__':
    # Calling function with integers as arguments and returns a value
    print(div(10, 5))

    # Diving by zero
    print(div(10, 0))

    # More neat value of handling
    result = div(10, 0)
    if result is None:
        print('Division by zero is undefined')
    else:
        print(result)
