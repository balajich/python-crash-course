'''
Simple class
'''


class Student:
    # This is an intialize method
    # Intializer is not constructor
    def __init__(self):
        self._name = 'Default Name'

    # This is a instance method
    def school(self):
        return 'public school'


if __name__ == "__main__":
    # Create an instance of class
    s = Student()

    # Access name attribute
    print(s._name)
