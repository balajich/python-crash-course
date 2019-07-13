'''IF statement
expr is converted to bool using bool() constructor
'''

if 0:
    print('This is False')

if 0.0:
    print('This is False')

if False:
    print('This is False')

if '':  # Empty String is False
    print('This is False')

if []:  # Empty collection is False
    print('This is False')

if 1:
    print('This is True')

if 1.0:
    print('This is True')

if True:
    print('This is True')

if 'a':
    print('This is True')

if 'False':  # Pay attention
    print('This is True')

if [1]:
    print('This is True')