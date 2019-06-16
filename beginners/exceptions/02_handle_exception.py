'''
Handle exception
'''


def convert(s):
    '''
    Covert String to an Integer
    :param s:
    :return:
    '''
    try:
        x = int(s)
    except ValueError:
        x = -1
    return x


if __name__ == "__main__":
    # Convert into String
    print(convert('10'))

    # This will return -1 because a cannot be converted and -1 is returned
    print(convert('a'))
