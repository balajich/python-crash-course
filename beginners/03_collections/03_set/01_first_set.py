'''
Set is a collection of unique elements
'''

if __name__ == "__main__":
    # Create set
    s = {1, 2, 3}
    print(s)

    # Create set using set function
    s = set()
    s.add(1)
    s.add(2)
    s.add(3)
    print(s)

    # Create a set from list
    s = set([1, 2, 3, 4, 1])  # Duplicates will be removed
    print(s)

    # set of characters
    s = set('HelloWorld')
    print(s)
