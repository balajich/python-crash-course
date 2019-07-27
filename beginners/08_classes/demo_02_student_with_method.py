'''
Simple class
'''


class Student:
    # This is a instance method
    def school(self):
        return 'public school'


if __name__ == "__main__":
    # Create an instance of class
    s = Student()

    # call the instance method
    print(s.school())

    # This is never used, we can call the methods using Class object
    print(Student.school(s))
