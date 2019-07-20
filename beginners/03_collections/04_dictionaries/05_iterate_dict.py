'''
Iterate dictionaries
'''

if __name__ == "__main__":
    d = {}  # Create empty dictornary
    d['Alex'] = 80
    d['Ram'] = 90
    print(d)

    # Iterate through dictionary
    for key, value in d.items():
        print(key, value)
