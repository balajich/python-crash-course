def convert(a):
    try:
        value=int(a)
        print('I am  excuted')
    except Exception as ex:
        raise ValueError
    return value


print(convert('10'))
print(convert(['abc']))
print(convert('abc'))
