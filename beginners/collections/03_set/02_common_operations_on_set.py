'''
Common operations on Sets like
- Iteration
- add or update
- remove
'''

if __name__ == "__main__":
    # Create set
    s = {1, 2, 3}
    print(s)
    s.add(4)  # add element
    print(s)
    s.update([5, 6])  # add more elements
    print(s)

    # find existence of an element in set
    print(3 in s)

    # Remove elements
    s.remove(1)
    print(s)

    a = {1, 2, 3}
    b = {3, 4}
    # Union
    print('Union: ', a | b)
    # Intersection
    print('Intersection: ', a & b)
    # Difference
    print('Difference: ', a - b)
