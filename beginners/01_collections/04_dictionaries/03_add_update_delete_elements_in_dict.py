'''
Operations on dictionary
'''

if __name__ == "__main__":
    # Create a students dictionary with their  marks in python. Here max mark is 100
    d = {"Joe": 80,
         "Alex": 90,
         "Ram": 10
         }
    # Print dictionary
    print(d)

    # Add and element in dictionary
    d['Nelly'] = 99
    print(d)

    # update an element in dictionary
    d['Ram'] = 89
    print(d)

    # Remove an element in dictionary
    del d['Ram']
    print(d)
