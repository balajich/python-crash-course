'''
Dictionaries are fundamental data structure where values are associated with keys

Dictionary keys must be immutable; in particular, you cannot use list s as keys. If
you need a multipart key, you should use a tuple or figure out a way to turn the key
into a string.
'''

if __name__ == "__main__":
    # Create a students dictionary with their  marks in python. Here max mark is 100
    d = {"Joe": 80,
         "Alex": 90,
         "Ram": 10
         }
    # Print dictionary
    print(d)

    # iterate to dictionary
    for key, value in d.items():
        print(key, value)
