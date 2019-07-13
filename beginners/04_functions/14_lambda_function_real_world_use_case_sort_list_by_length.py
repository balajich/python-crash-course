'''
Sorting a list of String by length instead of contents using lambda function
'''

if __name__ == '__main__':
    # list of string that needs to sorted by their length
    l = ['****', '$$$', '#', '--']
    # default implementation uses alphabetical ordering
    result = sorted(l)

    # print list
    for e in result:
        print(e)

    print('Sorting by length')
    # modify the default implementation by passing lambda function that uses length as key
    # instead of ascii value
    result = sorted(l, key=lambda x: len(x))
    # print list
    for e in result:
        print(e)
