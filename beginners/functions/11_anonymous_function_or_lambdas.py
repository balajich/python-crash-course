'''
create short anonymous functions, or lambdas
'''

if __name__ == '__main__':
    # create anonymous function add and call with arguments 10,20
    print((lambda a, b: a + b)(10, 20))

    # Anonymous function can be assigned to variable
    add = (lambda a, b: a + b)
    print(add(10, 20))
