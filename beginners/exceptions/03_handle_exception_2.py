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
        print('Conversion is successful')
    except ValueError:
        print('ValueError: Conversion failed')
        x = -1
    except TypeError:
        print(' Type Error: Conversion failed')
        x = -1
    return x


if __name__ == "__main__":
    # Convert into String
    print(convert('10'))

    # This will return -1 because a cannot be converted and -1 is returned
    print(convert('a'))

    # Try to convert list of strings to int. This will raise value error
    print(convert(['a']))
