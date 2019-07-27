'''
Python has special variable to identify whether we are running modules as scripts or using them
'''

print(__name__)

if __name__ == '__main__':
    print('I am invoked as script')
