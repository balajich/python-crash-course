'''
Common operations on lists
'''

if __name__ == "__main__":
    # Create list
    l = [1, 2, 3]
    print(l)

    # Append element last in list
    l.append(4)
    print(l)

    # Update first element in list
    l[0] = 0
    print(l)

    # delete first element in list
    del l[0]
    print(l)

    # Concatenate list
    l.extend([5, 6])
    print(l)

    # if you dont want to modify list l
    y = l + [7, 8]
    print(y)

    #length of list
    print(len(l))
