'''
Simple class
'''


class Student:
    def __init__(self):
        self._name = 'Default Name'

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # This is a instance method
    def school(self):
        return 'public school'


if __name__ == "__main__":
    # Create an instance of class
    s = Student()

    # Set name
    s.set_name('Alex')

    # Get name
    print(s.get_name())
