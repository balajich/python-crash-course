'''
Existence of element in dictionary
(i.e) Check for existence of key in dictionary
'''

if __name__ == '__main__':
    # Create a students dictionary with their  marks in python. Here max mark is 100
    d = {
        'Joe': 80,
        'Alex': 90,
        'Ram': 10
    }
    # Print dictionary
    print(d)

    print('Joe is in dictionary: ', 'Joe' in d)
    print('Neil is in dictionary: ', 'Neil' in d)

    # Try to get element where key doesnt exists
    try:
        d['Mogli']
    except KeyError:
        print('Key doesnt exists')

    # Dictionaries have a get method that returns a default value (instead of raising an exception)
    print(d.get('Mogli', 100))  # Mogli doesnt exist so 100 is returned
    print(d.get('Joe', 100))  # Joe already exist ,so his value 80 is returned
