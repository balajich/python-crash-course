'''
First exception
'''


def convert(s):
    '''
    Covert String to an Integer
    :param s:
    :return:
    '''
    x = int(s)
    return x


if __name__ == "__main__":
    # Convert into String
    print(convert('10'))

    # This will raise an exception
    print(convert('a'))
