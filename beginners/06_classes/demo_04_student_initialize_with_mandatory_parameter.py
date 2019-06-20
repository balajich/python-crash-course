'''
Simple class
'''


class Student:
    # This is an intialize method
    # Initializer is not constructor
    def __init__(self, name):
        if name is None:
            self._name = 'Default Name'
        else:
            self._name = name

    # This is a instance method
    def school(self):
        return 'public school'


if __name__ == "__main__":
    # Create an instance of class
    s = Student('Alex')

    # Access name attribute
    print(s._name)

    # Create an instance of class
    s = Student(None)

    # Access name attribute
    print(s._name)
